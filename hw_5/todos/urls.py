from django.urls import path
from .views import (
    login_view, logout_view, todo_list, todo_detail,
    todo_create, todo_delete
)

urlpatterns = [
    path('', todo_list, name='todo_list'),  # Список задач (только для авторизованных пользователей)
    path('<int:id>/', todo_detail, name='todo_detail'),  # Просмотр одной задачи
    path('new/', todo_create, name='todo_create'),  # Создание новой задачи
    path('<int:id>/delete/', todo_delete, name='todo_delete'),  # Удаление задачи
    path('login/', login_view, name='login'),  # Страница входа
    path('logout/', logout_view, name='logout'),  # Выход пользователя
]
