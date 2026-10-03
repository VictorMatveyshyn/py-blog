from django.db.models import Count
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views import generic

from blog.forms import AddCommentForm
from blog.models import Post


class IndexListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "post_list"
    paginate_by = 5
    queryset = Post.objects.all().annotate(comment_count=Count("commentary"))


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_queryset(self):
        return Post.objects.annotate(comment_count=Count("commentary"))

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context["form"] = AddCommentForm()
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.get(request, *args, **kwargs)

        self.object = self.get_object()  # отримуємо пост
        form = AddCommentForm(request.POST)  # створюємо форму з даних
        if form.is_valid():  # перевіряємо чи дані валідні
            commentary = form.save(commit=False)  # зберігаємо, але не в БД
            commentary.user = request.user  # додаємо користувача
            commentary.post = self.object  # додаємо пост
            commentary.save()  # зберігаємо в БД
        else:
            context = self.get_context_data(object=self.object, form=form)
            return self.get(request, *args, **kwargs)
        return self.get(request, *args, **kwargs)  # повертаємо сторінку
