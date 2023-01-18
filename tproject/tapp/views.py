from django.shortcuts import render
from .models import task

# Create your views here.
def add(request):
    if  request.method=="POST":
        name=request.POST.get('name','')
        priority=request.POST.get('priority','')
        Task=task(name=name,priority=priority)
        Task.save()
    return render(request,'home.html')
