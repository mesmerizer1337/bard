from django.shortcuts import render, get_object_or_404, redirect
from .models import Thread, Post
from .forms import ThreadForm, PostForm

# Список всех тем
def thread_list(request):
    threads = Thread.objects.all()
    return render(request, 'post/thread_list.html', {'threads': threads})

# Детали конкретной темы
def thread_detail(request, id):
    thread = get_object_or_404(Thread, id=id)
    posts = Post.objects.filter(thread=thread)
    return render(request, 'post/thread_detail.html', {'thread': thread, 'posts': posts})

# Удаление темы
def thread_delete(request, id):
    thread = get_object_or_404(Thread, id=id)
    if request.method == 'POST':
        thread.delete()
        return redirect('threads')  # Перенаправление на список тем
    return render(request, 'post/thread_confirm_delete.html', {'thread': thread})

# Редактирование темы
def thread_edit(request, id):
    thread = get_object_or_404(Thread, id=id)
    if request.method == 'POST':
        form = ThreadForm(request.POST, instance=thread)
        if form.is_valid():
            form.save()
            return redirect('thread_detail', id=thread.id)
    else:
        form = ThreadForm(instance=thread)
    return render(request, 'post/thread_form.html', {'form': form, 'thread': thread})

# Удаление поста
def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    thread_id = post.thread.id
    if request.method == 'POST':
        post.delete()
        return redirect('thread_detail', id=thread_id)  # Перенаправление на страницу темы
    return render(request, 'post/post_confirm_delete.html', {'post': post})

# Редактирование поста
def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('thread_detail', id=post.thread.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'post/post_form.html', {'form': form, 'post': post})
