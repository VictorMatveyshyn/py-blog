from django.db.models import Count
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views import generic

from blog.models import Post


class IndexListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "post_list"
    paginate_by = 5
    queryset = Post.objects.all().annotate(comment_count=Count("commentary"))


class PostDetailView(generic.DetailView):
    model = Post
