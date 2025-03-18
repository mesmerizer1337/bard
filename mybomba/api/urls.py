from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, index

# ������� ������ ��� �������������� ��������� ���������
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    path('', index, name='index'),  # ������� �������� API
]

# ��������� �������� �� �������
urlpatterns += router.urls
