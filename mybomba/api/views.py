from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Post
from .serializers import PostSerializer

def index(request):
    
    return JsonResponse({"message": "API working!"})

class PostViewSet(viewsets.ModelViewSet):
   
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Доступ для чтения всем, изменения — только авторизованным пользователям
