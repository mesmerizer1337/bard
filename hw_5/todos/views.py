# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Todo
from .forms import TodoForm

# ������� �������� (�������� �� todos/)
def home(request):
    return redirect('todo_list')

# �������� ������
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todo_list')  # ����� ����� �� ������ �����
        else:
            return render(request, 'login.html', {'error': 'Uncorrect Data'})

    return render(request, 'login.html')

# ����� ������������
def logout_view(request):
    logout(request)
    return redirect('login')

# ������ ����� ������������
@login_required
def todo_list(request):
    todos = Todo.objects.filter(user=request.user)
    return render(request, 'todos/list.html', {'todos': todos})

# ������ ����� ������
@login_required
def todo_detail(request, id):
    todo = get_object_or_404(Todo, id=id, user=request.user)
    return render(request, 'todos/detail.html', {'todo': todo})

# �������� ����� ������
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

# �������� ������ (������ �����)
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

# ������� �������� (�������� �� todos/)
def home(request):
    return redirect('todo_list')

# �������� ������
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todo_list')  # ����� ����� �� ������ �����
        else:
            return render(request, 'login.html', {'error': 'uncorrect data'})

    return render(request, 'login.html')

# ����� ������������
def logout_view(request):
    logout(request)
    return redirect('login')

# ������ ����� ������������
@login_required
def todo_list(request):
    todos = Todo.objects.filter(user=request.user)
    return render(request, 'todos/list.html', {'todos': todos})

# ������ ����� ������
@login_required
def todo_detail(request, id):
    todo = get_object_or_404(Todo, id=id, user=request.user)
    return render(request, 'todos/detail.html', {'todo': todo})

# �������� ����� ������
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

# �������� ������ (������ �����)
@login_required
def todo_delete(request, id):
    todo = get_object_or_404(Todo, id=id)

    if todo.user != request.user:
        return HttpResponseForbidden("U cant del this goal!")

    todo.delete()
    return redirect('todo_list')
