from django.shortcuts import render, redirect, reverse
from .models import *
from django.views.generic import View
from django.core.exceptions import ValidationError
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from .utils import *
from .forms import TagForm, PostForm

# Create your views here.
def home(request):
    return redirect('blog', permanent=True)

def homeBlog(request):
    search = request.GET.get('search', '')
    if search:
        data = reversed(Post.objects.filter(Q(title__icontains=search) | Q(body__icontains=search)))
    else:
        data = reversed(Post.objects.all())
    return render(request, 'blog/index.html', {'data': data})

def getTags(request):
    search = request.GET.get('search', '')
    if search:
        data = Tag.objects.filter(Q(title__icontains=search) | Q(title__icontains=search))
    else:
        data = Tag.objects.all()
    return render(request, 'blog/tags.html', {'data': data})

class GetPost(ModelDetailsMixin, View):
    model = Post
    template = 'blog/getPost.html'
    
class GetTag(ModelDetailsMixin, View):
    model = Tag
    template = 'blog/getTag.html'

class CreateTag(LoginRequiredMixin,CreateDetailsMixin, View):
    form = TagForm()
    url = 'tag.html'
    raise_exception = True

class CreatePost(LoginRequiredMixin, CreateDetailsMixin, View):
    form = PostForm()
    url = 'Post.html'
    raise_exception = True

class UpdateTag(LoginRequiredMixin, UpdateObjectMixin, View):
    model = Tag
    template = 'blog/updateTag.html'
    Form = TagForm
    raise_exception = True
        
class UpdatePost(LoginRequiredMixin, UpdateObjectMixin, View):
    model = Post
    template = 'blog/updatePost.html'
    Form = PostForm
    raise_exception = True

class DeleteTag(LoginRequiredMixin, DeleteObjectMixin, View):
    model = Tag
    template = 'blog/deleteTag.html'
    rev = 'getTags'
    raise_exception = True
    
class DeletePost(LoginRequiredMixin, DeleteObjectMixin, View):
    model = Post
    template = 'blog/deletePost.html'
    rev = 'blog'
    raise_exception = True
