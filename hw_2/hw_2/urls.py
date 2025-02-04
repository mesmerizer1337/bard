from django.contrib import admin
from django.urls import path
from movie.views import movie_list, movie_detail
from blog.views import article_list, article_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', movie_list, name='movie_list'),
    path('movies/<int:id>/', movie_detail, name='movie_detail'),
    path('articles/', article_list, name='article_list'),
    path('articles/<int:id>/', article_detail, name='article_detail'),
]
