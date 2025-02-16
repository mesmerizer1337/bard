from django.shortcuts import render, get_object_or_404, redirect
from .models import TodoList, Todo

def redirect_to_todo_lists(request):
    return redirect('todo_lists')

def todo_lists(request):
    lists = TodoList.objects.all()
    return render(request, 'todos/todo_lists.html', {'lists': lists})

def todo_list_detail(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    todos = todo_list.todo_set.all()
    return render(request, 'todos/todo_list_detail.html', {'todo_list': todo_list, 'todos': todos})
