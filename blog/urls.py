from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="starting-page"),
    path("posts", views.posts, name="posts-page"),
    path("posts/<slug:post_identifier>", views.post_details, name="post-detail-page"),
]
