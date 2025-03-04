from django.db import models
from django.contrib.auth.models import User
from reservations.models import Reservation 

class ForumThread(models.Model):
    title = models.CharField(max_length=255)
    reservation = models.OneToOneField(Reservation, on_delete=models.CASCADE, related_name="forum_thread", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class ForumPost(models.Model):
    thread = models.ForeignKey(ForumThread, on_delete=models.CASCADE, related_name="posts")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
