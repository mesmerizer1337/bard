from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('notes/', include('note.urls')),

    # ��������������� � "/" �� "/notes/"
    path('', lambda request: redirect('note_list')),
]
