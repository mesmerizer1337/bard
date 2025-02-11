from django.urls import path
from . import views

app_name = 'todos'

urlpatterns = [
    path('', views.TodoList.as_view(), name='todo_list'),
    path('<int:id>/', views.TodoDetail.as_view(), name='todo_detail'),
    path('create/', views.TodoCreate.as_view(), name='todo_create'),
    path('<int:id>/delete/', views.TodoDetail.as_view(), name='todo_delete'),
]
