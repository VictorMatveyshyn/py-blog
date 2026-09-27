from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from blog.models import Post

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    # post_list = Post.objects.all()
    #
    # context = {
    #     "post_list": post_list,
    # }

    return render(request, "blog/index.html") #, context=context)
