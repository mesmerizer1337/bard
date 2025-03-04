from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include("mt.home_urls")), 
    path("admin/", admin.site.urls),
    path("customers/", include("customers.urls")),
    path("tables/", include("tables.urls")),
    path("reservations/", include("reservations.urls")),
    path('forums/', include('forums.urls')),  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
