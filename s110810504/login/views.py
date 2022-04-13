from email import message
from django.http import HttpResponse
from django.contrib import auth
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# Create your views here.
def login_add_user(request):
    try: 
        user = User.objects.get(username='test')
    except:
        user = None
    if user !=None:
        message = user.username + 'account already create!'
        return HttpResponse(message)
    else:
        user = User.objects.create_user('test','test@test.com.tw','a123456')
        user.first_name = 'wen'
        user.last_name = 'lin'
        user.is_staff = True
        user.save()
        return redirect('/admin/')

def login_index(request):
    if request.user.is_authenticated:
        name = request.user.username
    return render(request,'login/index.html',locals())

def login_login(request):
    if request.method =='POST':
        name = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=name,password=password)
        if user is not None:
            if user.is_active:
                auth.login(request,user)
                return redirect('/login/index/')
                message = 'login success'
            else:
                message = 'account not valid'
        else: 
            message = 'login failed'
    return render(request,'login/login.html',locals())

def login_logout(request):
    auth.logout(request)
    return redirect('/login/index/')