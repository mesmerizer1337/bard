from django.urls import path
from .views import forum_list, forum_thread, create_thread, create_post

urlpatterns = [
    path('', forum_list, name='forum_list'),  # ������ ���� ���
    path('<int:thread_id>/', forum_thread, name='forum_thread'),  # �������� ���������� ����
    path('create/', create_thread, name='create_thread'),  # �������� ����� ����
    path('<int:thread_id>/post/', create_post, name='create_post'),  # �������� ����� � ����
]
