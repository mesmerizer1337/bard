from django.contrib import admin
from django.urls import path, include
from todos.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todos/', include('todos.urls')),
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),  # Добавляем маршруты аутентификации
]
