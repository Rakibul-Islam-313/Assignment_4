from django.shortcuts import render
from tasks . models import MyTask
def add_show(request):
    data = MyTask.objects.all()
    return render(request,'show.html', {'data': data})