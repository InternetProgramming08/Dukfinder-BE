from django.db import models
from django.contrib.auth.models import User
import os

class NoticePost(models.Model):
    title = models.CharField(max_length=30, blank=True)

    content = models.TextField()

    head_image = models.ImageField(upload_to='notice/images/%Y/%m/%d/', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.author}'

    def get_absolute_url(self):
        return f'/notice/{self.pk}/'