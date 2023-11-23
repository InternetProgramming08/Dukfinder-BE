from django.db import models
from django.contrib.auth.models import User
import os
class FindCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/category/{self.slug}/'

    class Meta:
        verbose_name_plural = 'categories'

class FindLocation(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/locations/{self.slug}/'

    class Meta:
        verbose_name_plural = 'locations'


class Post(models.Model):
    title = models.CharField(max_length=30, blank=True)

    category = models.ForeignKey(FindCategory, null=True, blank=True, on_delete=models.SET_NULL)
    location = models.ForeignKey(FindLocation, null=True, blank=True, on_delete=models.SET_NULL)
    content = models.TextField()

    head_image = models.ImageField(upload_to='find/images/%Y/%m/%d/', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    date_select = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.author}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'



class FindComment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField(max_length=100)

    parent = models.ForeignKey('self', related_name='reply', on_delete=models.CASCADE, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author}::{self.content}'