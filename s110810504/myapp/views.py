from django.shortcuts import render
from myapp.models import student
# Create your views here.
def list_one(request):
    try:
        unit = student.objects.get(Name='aaa')
    except:
        error_message = 'data reading errors'
    return render(request,'myapp/list_one.html',locals())

def list_all(request):
    students = student.objects.all().order_by('id')
    return render(request,'myapp/list_all.html',locals())
def list_index(request):
    students = student.objects.all().order_by('id')
    return render(request,'myapp/list_index.html',locals())