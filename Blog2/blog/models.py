from django.db import models
from datetime import datetime
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time

# Create your models here.

def slugg(slg):
    slg = slugify(slg, allow_unicode=True)
    return slg + str(int(time()))

class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(unique=True, max_length=150)
    body = models.TextField(blank=True, db_index=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    date_pub = models.DateTimeField(default=datetime.now)

    def get_absolute_url(self):
        return reverse('getPost', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugg(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.title)
    
    def get_updated_url(self):
        return reverse('updatePost', kwargs={'slug': self.slug})
    
    def get_deleted_url(self):
        return reverse('deletePost', kwargs={'slug': self.slug})

class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return '{}'.format(self.title)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugg(self.title)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('getTag', kwargs={'slug': self.slug})
    
    def get_updated_url(self):
        return reverse('updateTag', kwargs={'slug': self.slug})

    def get_deleted_url(self):
        return reverse('deleteTag', kwargs={'slug': self.slug})