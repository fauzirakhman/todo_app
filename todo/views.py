from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Task

# Create your views here.
def addTask(request):
    print (request.POST['task'])
    task = request.POST['task']
    Task.objects.create(task=task)
    
    # return HttpResponse('The form is submitted')
    return redirect('home')