from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

# Корневой обработчик для проверки работы API
def home(request):
    return JsonResponse({"message": "API is running"})

urlpatterns = [
    path('admin/', admin.site.urls),  # Админ-панель
    path('', home, name='home'),  # Корневой маршрут, возвращающий JSON-ответ
    path('api/', include('api.urls')),  # Подключаем маршруты приложения `api`

    # JWT-аутентификация
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
