from unicodedata import category
from django.shortcuts import render,redirect
from newsapp import models
import math
from django.contrib import auth
from django.contrib.auth import authenticate
# Create your views here.
page1  =1 

def news_index(request,pageindex=None):
    global page1
    pagesize = 8
    newsall = models.NewsUnit.objects.all().order_by('-id')
    datasize = len(newsall)
    totpage = math.ceil(datasize / pagesize)
    if pageindex == None:
        page1 = 1
        newsunits = models.NewsUnit.objects.filter(enabled = True).order_by('-id')[:pagesize]

    elif pageindex == '1':
        start = (page1 - 2) * pagesize
        if start >= 0:
            newsunits = models.NewsUnit.objects.filter(enabled=True).order_by('-id')[start:(start + pagesize)]
            page1 -= 1

    elif pageindex == '2':
        start = page1 * pagesize
        if start < datasize:
            newsunits = models.NewsUnit.objects.filter(enabled = True).order_by('-id')[start:(start + pagesize)]
            page1 += 1

    elif pageindex == '3':
        start = (page1 - 1) * pagesize
        newsunits = models.NewsUnit.objects.filter(enabled = True).order_by('-id')[start:(start + pagesize)]

    currentpage = page1
    return render(request, 'news/index.html', locals())


def news_detail(request,detailid = None):
    unit = models.NewsUnit.objects.get(id = detailid)
    category = unit.catego
    title = unit.title
    pubtime = unit.pubtime
    nickname = unit.nickname
    message = unit.message
    unit.press += 1
    unit.save()

    return render(request, 'news/detail.html', locals())

def news_login(request):
    messages = ''
    if request.method =='POST':
        name = request.POST['username'].strip()
        password = request.POST['password']
        user1 = authenticate(username = name , password = password)
        if user1 is not None:
            if user1.is_active:
                auth.login(request,user1)
                return redirect('/news/adminmain/')
            else:
                messages = 'account invalid'
        else:
            messages = 'login failed'
    return render(request,'news/login.html',locals())

def news_logout(request):
    auth.logout(request)
    return redirect('/news/index/')

def news_adminmain(request,pageindex=None):
    global page1
    pagesize =8 
    newsall  = models.NewsUnit.objects.all().order_by('-id')
    datasize = len(newsall)
    totpage = math.ceil(datasize/pagesize)
    if pageindex == None:
        page1 = 1
        newsunits = models.NewsUnit.objects.order_by('-id')[:pagesize]
    elif pageindex =='1':
        start = (page1 -2)*pagesize
        if start >=0:
            newsunits = models.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
            page1-=1
    elif pageindex =='2':
        start = page1*pagesize
        if start < datasize:
            newsunits = models.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
            page+=1
    elif pageindex =='3':
        start=(page1-1)*pagesize
        newsunits = models.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
    currentpage = page1
    return render(request,'news/adminmain.html',locals())    

def news_newsadd(request):
    message = ''
    category = request.POST.get('news_type','')
    subject = request.POST.get('news_subject','')
    editor = request.POST.get('news_editor','')
    content = request.POST.get('news_content','')
    ok = request.POST.get('news_ok','')
    if subject =='' or editor=='' or content =='':
        message = 'subject and editor and content must write'
    else:
        if ok =='yes':
            enabled = True
        else:
            enabled =False
        unit = models.NewsUnit.objects.create(catego = category , nickname = editor, title=subject,message = content, enabled = enabled , press =0)
        unit.save()
        return redirect('/news/adminmain')
    return render(request,'news/newsadd.html',locals())

def news_newsedit(request, newsid=None,edittype=None):
    unit = models.NewsUnit.objects.get(id = newsid)
    categories = ['公告','更新','活動','其他']
    if edittype == None:
        type = unit.catego
        subject = unit.title
        editor = unit.nickname
        content = unit.message
        ok = unit.enabled
    elif edittype =='1':
        category = request.POST.get('news_type','')
        subject = request.POST.get('news_subject','')
        editor = request.POST.get('news_editor','')
        content = request.POST.get('news_content','')
        ok = request.POST.get('news_ok','')
        if ok =='yes':
            enabled = True
        else:
            enabled = False
        unit.catego = category
        unit.nickname = editor
        unit.title = subject
        unit.message = content
        unit.enabled = enabled
        unit.save()
        return redirect('/news/adminmain')
    return render(request,'news/newsedit.html',locals())

def news_newsdelete(request,newsid = None , deletetype = None):
    unit = models.NewsUnit.objects.get(id=newsid)
    if deletetype == None:
        type = str(unit.catego.strip())
        subject = unit.title
        editor = unit.nickname
        content = unit.message
        date = unit.pubtime

    elif deletetype =='1':
        unit.delete()
        return redirect('/news/adminmain/')
    return render(request,'news/newsdelete.html',locals())