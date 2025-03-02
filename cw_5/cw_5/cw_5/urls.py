from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('post_list')),  # Главная перенаправляет на посты
    path('', include('posts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # Добавляет стандартные страницы аутентификации
]
