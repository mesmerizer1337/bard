from django.urls import path
from .views import forum_list, forum_thread, create_thread, create_post

urlpatterns = [
    path('', forum_list, name='forum_list'),  # Список всех тем
    path('<int:thread_id>/', forum_thread, name='forum_thread'),  # Просмотр конкретной темы
    path('create/', create_thread, name='create_thread'),  # Создание новой темы
    path('<int:thread_id>/post/', create_post, name='create_post'),  # Создание поста в теме
]
