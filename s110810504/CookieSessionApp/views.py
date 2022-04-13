from django.http import HttpResponse
from django.shortcuts import render
import datetime
# Create your views here.
def set_cookie(request,key=None,value=None):
    response = HttpResponse('cookie stored')
    response.set_cookie(key,value)
    return response

def set_cookie2(request,key=None,value=None):
    response = HttpResponse('limited time :1 hour')
    response.set_cookie(key,value,max_age=3600)
    return response

def get_cookie(request,key=None):
    if key in request.COOKIES:
        return HttpResponse('%s : %s'%(key,request.COOKIES[key]))
    else:
        return HttpResponse('Cookie invalid')

def get_all_cookies(request,kry=None):
    print('get_all_cookies() is invoked')
    if request.COOKIES != None:
        strcookies = ''
        for k1,v1 in request.COOKIES.items():
            strcookies = strcookies +k1 + ':' + v1 + '<br>'
        return HttpResponse('%s'%(strcookies))
    else:
        return HttpResponse('cookie not exist')
def delete_cookie(request,key=None):
    if key in request.COOKIES:
        response = HttpResponse('Delete Cookie:'+key)
        response.delete_cookie(key)
        return response
    else:
        return HttpResponse('No cookies:'+key)

def CookieSessionApp_index(request):
    if 'counter' in request.COOKIES:
        counter = int(request.COOKIES['counter'])
        counter += 1
    else:
        counter = 1
    response = HttpResponse('today times'+ str(counter))
    tomorrow = datetime.datetime.now()+ datetime.timedelta(days=1)
    tomorrow = datetime.datetime.replace(tomorrow,hour=0,minute=0,second=0)
    expires = datetime.datetime.strftime(tomorrow, '%a,%d-%b-%y %H:%M:%S GMT')
    response.set_cookie('counter',counter,expires = expires)
    return response

def set_session(request,key=None,value=None):
    response = HttpResponse('Session store finished')
    request.session[key] = value
    return response

def get_session(request,key=None):
    if key in request.session:
        return HttpResponse('%s : %s'%(key,request.session[key]))
    else:
        return HttpResponse('Session invalid')

def get_all_sessions(request):
    if request.session != None:
        if request.session != None:
            strsessions = ''
            for key1,value1 in request.session.items():
                strsessions = strsessions +key1 +":" + str(value1) + '<br>'
            return HttpResponse(strsessions)
        else:
            return HttpResponse('strsessions invalid')


def vote(request):
    if not 'vote' in request.session:
        request.session['vote'] = True
        msg = 'first vote'
    else:
        msg = 'already vote'
    
    response = HttpResponse(msg)
    return response
def set_session2(request,key=None,value=None):
    response = HttpResponse('Session storing finished')
    request.session[key] = value
    request.session.set_expiry(30)
    return response 

def login(request):
    username='rick'
    password='12345'
    if request.method =='POST':
        if not 'username' in request.session:
            if request.POST['username'] == username and request.POST['password'] == password:
                request.session['username'] = username
                message = 'welcome' + username
                status = 'login'
    else: 
        if 'username' in request.session:
            if request in request.session:
                if request.session['username']== username:
                    message = request.session['username'] + 'already login'
                    status = 'login'
    return render(request,'CookieSessionApp/login.html',locals())

def logout(request):
    if 'username' in request.session:
        message = request.session['username']+'already logout'
        del request.session['username']
    return render(request,'CookieSessionApp/login.html',locals())        