from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=255)  # Заголовок поста
    content = models.TextField()  # Текст поста
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Автор поста
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания
    updated_at = models.DateTimeField(auto_now=True)  # Дата обновления

    def __str__(self):
        return self.title
