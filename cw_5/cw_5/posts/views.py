from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from .models import Post
from .forms import PostForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Исправлено (get безопаснее)
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('post_list')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

@login_required
def my_posts(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, 'post_list.html', {'posts': posts})

@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    is_author = request.user == post.author
    is_superuser = request.user.is_superuser
    return render(request, 'post_detail.html', {
        'post': post,
        'is_author': is_author,
        'is_superuser': is_superuser
    })

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form': form})

@login_required
@csrf_exempt  # Разрешает DELETE-запросы
def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user == post.author or request.user.is_superuser:
        post.delete()
        return redirect('post_list')
    return HttpResponseForbidden()
