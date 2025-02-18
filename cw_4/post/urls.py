from django.urls import path
from . import views

urlpatterns = [
    path('', views.thread_list, name='threads'),  # Список всех тем
    path('threads/<int:id>/', views.thread_detail, name='thread_detail'),  # Детали темы
    path('threads/<int:id>/delete/', views.thread_delete, name='thread_delete'),  # Удаление темы
    path('threads/<int:id>/edit/', views.thread_edit, name='thread_edit'),  # Редактирование темы
    path('posts/<int:id>/delete/', views.post_delete, name='post_delete'),  # Удаление поста
    path('posts/<int:id>/edit/', views.post_edit, name='post_edit'),  # Редактирование поста
]
