from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirect_to_todo_lists),  # Перенаправление на /todo-lists
    path('todo-lists/', views.todo_lists, name='todo_lists'),
    path('todo-lists/<int:id>/', views.todo_list_detail, name='todo_list_detail'),
]
