from django.urls import path
from . import views

urlpatterns = [
    path('', views.thread_list, name='thread_list'),
    path('threads/<int:thread_id>/', views.thread_detail, name='thread_detail'),
    path('threads/create/', views.thread_create, name='thread_create'),
    path('threads/<int:thread_id>/delete/', views.thread_delete, name='thread_delete'),
    path('posts/<int:thread_id>/create/', views.post_create, name='post_create'),
    path('posts/<int:post_id>/delete/', views.post_delete, name='post_delete'),
]
