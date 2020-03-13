from django.shortcuts import render, redirect
from base.models import Task
from base.forms import TaskForm
# Create your views here.

def Home(request):
    tasks = Task.objects.all()
    forms = TaskForm()
    if request.method == "POST":
        forms = TaskForm(request.POST)
        if forms.is_valid():
            forms.save()
        return redirect('/')
    context = {"tasks": tasks, 'forms': forms}
    return render(request, 'base/home.html', context)

def UpdatePage(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={"form":form}
    return render(request, 'base/update.html', context)

def DeletePage(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == "POST":
        task.delete()
        return redirect('/')
    context={'task': task}
    return render(request, 'base/delete.html', context)
