from django.urls import path
from blog.views import IndexListView, PostDetailView

urlpatterns = [
    path("", IndexListView.as_view(), name="index"),
    path("detail/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
]
app_name = "blog"
