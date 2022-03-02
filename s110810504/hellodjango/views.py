from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# test1
def hello_world(request):
    return HttpResponse('helloworld')

# test2
def hello_user(request,username):
    return HttpResponse('hello '+ username)

# test3
def hello_template(request,username):
    now = datetime.now()
    #ycl=calendar.TextCalendar()
    #year_calendar= ycl.formatyear(2022,c=3, m=4)
    return render(request,"hi.html",{
        'now': now ,
        'username': username,
    })
#test4
def hello_static(request,username):
    now = datetime.now()
    return render(request,"hii.html",{
        'now': now ,
        'username': username,
    })
