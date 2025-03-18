from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

# �������� ���������� ��� �������� ������ API
def home(request):
    return JsonResponse({"message": "API is running"})

urlpatterns = [
    path('admin/', admin.site.urls),  # �����-������
    path('', home, name='home'),  # �������� �������, ������������ JSON-�����
    path('api/', include('api.urls')),  # ���������� �������� ���������� `api`

    # JWT-��������������
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
