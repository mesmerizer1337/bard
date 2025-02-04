from django.shortcuts import render, get_object_or_404
from .models import Movie

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/list.html', {'movies': movies})

def movie_detail(request, id):
    movie = get_object_or_404(Movie, id=id)
    return render(request, 'movies/detail.html', {'movie': movie})