from django.urls import path
from .views import (
    login_view, logout_view, todo_list, todo_detail,
    todo_create, todo_delete
)

urlpatterns = [
    path('', todo_list, name='todo_list'),  # ������ ����� (������ ��� �������������� �������������)
    path('<int:id>/', todo_detail, name='todo_detail'),  # �������� ����� ������
    path('new/', todo_create, name='todo_create'),  # �������� ����� ������
    path('<int:id>/delete/', todo_delete, name='todo_delete'),  # �������� ������
    path('login/', login_view, name='login'),  # �������� �����
    path('logout/', logout_view, name='logout'),  # ����� ������������
]
