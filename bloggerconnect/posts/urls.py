from django.urls import path
from . import views

urlpatterns = [
    path("", views.posts, name="posts"),
    path("post/<str:pk>/", views.post, name="post"),
]
