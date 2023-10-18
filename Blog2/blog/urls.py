from django.urls import path
from .views import *

urlpatterns = [
    path('', homeBlog, name='blog'),
    path('post/createpost', CreatePost.as_view(), name='createPost'),
    path('post/<str:slug>', GetPost.as_view(), name='getPost'),
    path('post/<str:slug>/update', UpdatePost.as_view(), name='updatePost'),
    path('post/<str:slug>/delete', DeletePost.as_view(), name='deletePost'),
    path('tags', getTags, name='getTags'),
    path('tag/createtag', CreateTag.as_view(), name='createTag'),
    path('tag/<str:slug>', GetTag.as_view(), name='getTag'),
    path('tag/<str:slug>/update', UpdateTag.as_view(), name='updateTag'),
    path('tag/<str:slug>/delete', DeleteTag.as_view(), name='deleteTag'),
]