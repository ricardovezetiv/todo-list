from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from django.contrib import messages


def home(request):
    if request.method == 'POST':
        form = TodoForm(request.POST or None)

        if form.is_valid():
            form.save()
            todos = Todo.objects.all()
            messages.success(request, ('Task has been added!'))
            return render(request, 'todo_app/home.html', {'todos': todos})
    else:
        todos = Todo.objects.all()
        return render(request, 'todo_app/home.html', {'todos': todos})


def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    messages.success(request, ('Task has been Deleted!'))
    return redirect('home')


def task_complete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = True
    todo.save()
    return redirect('home')


def task_incomplete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = False
    todo.save()
    return redirect('home')
