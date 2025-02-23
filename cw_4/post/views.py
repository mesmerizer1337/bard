from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Thread, Post
from .forms import PostForm, ThreadForm

def thread_list(request):
    """Список всех тем (Thread)"""
    threads = Thread.objects.all().order_by('-created_at')
    return render(request, 'post/thread_list.html', {'threads': threads})

def thread_detail(request, thread_id):
    """Детальная страница темы (Thread)"""
    thread = get_object_or_404(Thread, id=thread_id)
    posts = thread.posts.all().order_by('created_at')  # Исправленный related_name в модели Post
    return render(request, 'post/thread_detail.html', {'thread': thread, 'posts': posts})

@login_required
def thread_create(request):
    """Создание новой темы (Thread)"""
    if request.method == "POST":
        form = ThreadForm(request.POST)
        if form.is_valid():
            thread = form.save()
            messages.success(request, "Тема успешно создана.")
            return redirect('thread_detail', thread_id=thread.id)
    else:
        form = ThreadForm()

    return render(request, 'post/thread_form.html', {'form': form})

@login_required
def thread_delete(request, thread_id):
    """Удаление темы (Thread)"""
    thread = get_object_or_404(Thread, id=thread_id)
    
    if request.method == "POST":
        thread.delete()
        messages.success(request, "Тема успешно удалена.")
        return redirect('thread_list')

    return render(request, 'post/thread_confirm_delete.html', {'thread': thread})

@login_required
def post_create(request, thread_id):
    """Создание нового поста (Post) в теме"""
    thread = get_object_or_404(Thread, id=thread_id)

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.thread = thread
            post.author = request.user  # Автор поста - текущий пользователь
            post.save()
            messages.success(request, "Пост успешно добавлен.")
            return redirect('thread_detail', thread_id=thread.id)
    else:
        form = PostForm()

    return render(request, 'post/post_form.html', {'form': form, 'thread': thread})

@login_required
def post_delete(request, post_id):
    """Удаление поста (Post)"""
    post = get_object_or_404(Post, id=post_id)
    thread_id = post.thread.id  # Сохраняем id темы перед удалением

    if request.method == "POST":
        post.delete()
        messages.success(request, "Пост успешно удален.")
        return redirect('thread_detail', thread_id=thread_id)

    return render(request, 'post/post_confirm_delete.html', {'post': post})
