from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Thread(models.Model):
    """Thread model"""
    name = models.CharField(max_length=255, verbose_name="Name")
    description = models.TextField(verbose_name="Description")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    def __str__(self):
        return self.name


class Post(models.Model):
    """Post model"""
    title = models.CharField(max_length=255, verbose_name="Title")
    picture = models.FileField(upload_to='post_pictures/', blank=True, null=True, verbose_name="Picture")
    description = models.TextField(verbose_name="Description")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Author")
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name="posts", verbose_name="Thread")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    def __str__(self):
        return f'Post in {self.thread.name} - {self.created_at.strftime("%Y-%m-%d %H:%M")} by {self.author.username}'
