from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, index

# Создаем роутер для автоматической генерации маршрутов
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    path('', index, name='index'),  # Главная страница API
]

# Добавляем маршруты из роутера
urlpatterns += router.urls
