from django.shortcuts import render, get_object_or_404, redirect
from .forms import TagForm as Tform
from .forms import PostForm as Pform
from .models import *

class ModelDetailsMixin:
    model = None
    template = None

    def get(self, request, slug):
        data = get_object_or_404(self.model, slug=slug)
        return render(request, self.template, {'data': data})
    
class CreateDetailsMixin():
    def get(self, request):
        form = None
        url = None
        template = f'blog/create{self.url}'
        return render(request, template, {'data': self.form})
    
    def post(self, request):
        url = None
        template = f'blog/create{url}'
        if request.POST.get('body') == None:
            boundForm = Tform(request.POST)
        elif request.POST.get('body') != None:
            boundForm = Pform(request.POST)
        if boundForm.is_valid():
            new = boundForm.save()
            return redirect(new)
        return render(request, template, {'data': self.boundForm})
    
class UpdateObjectMixin():
    model = None
    template = None
    Form = None
    def get(self, request,slug):
        obj = self.model.objects.get(slug=slug)
        boundForm = self.Form(instance=obj)
        return render(request, self.template, {'data':boundForm, 'obj': obj})
    
    def post(self, request, slug):
        obj = self.model.objects.get(slug=slug)
        boundForm = self.Form(request.POST, instance=obj)

        if boundForm.is_valid():
            newObj = boundForm.save()
            return redirect(newObj)
        return render(request, self.template, {'data':boundForm, 'obj': newObj})
    
class DeleteObjectMixin():
    model = None
    template = None
    rev = None
    def get(self, request, slug):
        obj = self.model.objects.get(slug=slug)
        return render(request, self.template, {'data': obj})
    
    def post(self, request, slug):
        obj = self.model.objects.get(slug=slug)
        obj.delete()
        return redirect(reverse(self.rev))