from django.shortcuts import render,redirect,get_object_or_404
from tasks.models import TASK
from tasks.forms import TASKFORM
import datetime

# Create your views here.

def view_all_tasks(request):
    obj = TASK.objects.all()
    return render(request,'tasks/index.html',{'data':obj})

def time(request):
    date = datetime.datetime.now()
    date_dict ={'display_date':date}
    return render(request,'tasks/time.html',context=date_dict)


def add_task(request):
    if request.method == 'POST':
        form = TASKFORM(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TASKFORM()
    context = {
        'form':form
    }
    return render(request,'tasks/add_task.html',context)

def edit_task(request,id):
    obj =TASK.objects.get(id=id)
    if request.method == 'POST':
        form = TASKFORM(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TASKFORM(instance=obj)
    context = {
            'form':form
        }
    return render(request,'tasks/edit_task.html',context)

def delete_task(request,id):
    obj = get_object_or_404(TASK,id=id)
    obj.delete()
    return redirect ('home')
    
def get_task_by_id(request,id):
    task = get_object_or_404(TASK,id=id)
    return render(request,'tasks/get_task.html',{'task':task})

def filter_task_by_priority(request,priority):
    tasks = TASK.objects.filter(id=priority)
    return render(request,'tasks/filter_task.html',{'tasks':tasks})
  