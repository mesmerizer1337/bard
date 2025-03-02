# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Todo
from .forms import TodoForm

# Главная страница (редирект на todos/)
def home(request):
    return redirect('todo_list')

# Страница логина
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todo_list')  # После входа на список задач
        else:
            return render(request, 'login.html', {'error': 'Uncorrect Data'})

    return render(request, 'login.html')

# Выход пользователя
def logout_view(request):
    logout(request)
    return redirect('login')

# Список задач пользователя
@login_required
def todo_list(request):
    todos = Todo.objects.filter(user=request.user)
    return render(request, 'todos/list.html', {'todos': todos})

# Детали одной задачи
@login_required
def todo_detail(request, id):
    todo = get_object_or_404(Todo, id=id, user=request.user)
    return render(request, 'todos/detail.html', {'todo': todo})

# Создание новой задачи
@login_required
def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm()

    return render(request, 'todos/form.html', { 'form': form})

# Удаление задачи (только своей)
@login_required
def todo_delete(request, id):
    todo = get_object_or_404(Todo, id=id)

    if todo.user != request.user:
        return HttpResponseForbidden("u cant del this goal")

    todo.delete()
    return redirect('todo_list')
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Todo
from .forms import TodoForm

# Главная страница (редирект на todos/)
def home(request):
    return redirect('todo_list')

# Страница логина
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todo_list')  # После входа на список задач
        else:
            return render(request, 'login.html', {'error': 'uncorrect data'})

    return render(request, 'login.html')

# Выход пользователя
def logout_view(request):
    logout(request)
    return redirect('login')

# Список задач пользователя
@login_required
def todo_list(request):
    todos = Todo.objects.filter(user=request.user)
    return render(request, 'todos/list.html', {'todos': todos})

# Детали одной задачи
@login_required
def todo_detail(request, id):
    todo = get_object_or_404(Todo, id=id, user=request.user)
    return render(request, 'todos/detail.html', {'todo': todo})

# Создание новой задачи
@login_required
def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm()

    return render(request, 'todos/form.html', {'form': form})

# Удаление задачи (только своей)
@login_required
def todo_delete(request, id):
    todo = get_object_or_404(Todo, id=id)

    if todo.user != request.user:
        return HttpResponseForbidden("U cant del this goal!")

    todo.delete()
    return redirect('todo_list')
