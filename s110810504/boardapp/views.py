from django.shortcuts import render,redirect
from boardapp import models,forms
from django.contrib.auth import authenticate
from django .contrib import auth
from django.contrib import math

from s110810504.myapp.views import postform
# Create your views here.
page =0

def board_index(request,pageindex=None):
    global page
    pagesize =3 
    boardall = models.BoardUnit.objects.all().oreder_by('-id')
    datasize = len(boardall)
    totpage = math.ceil(datasize/pagesize)
    if pageindex ==None:
        page = 0
        boardunits = models.BoardUnit.objects.order_by('-id')[:pagesize]
    elif pageindex == 'prev':
        start = (page-1)*pagesize
        if start>=0:
            boardunits = models.BoardUnit.objects.order_by('-id')[start:(start+pagesize)]
            page-=1
    elif pageindex == 'next':
        start = (page+1)*pagesize
        if start<datasize:
            boardunits = models.BoardUnit.objects.order_by('-id')[start:(start+pagesize)]
            page+=1
    currentpage = page +1
    return render(request,'board/index.html')
        
def post(request):
    if request.method =='POST':
        postform = forms.PostForm(request.POST)
        if postform.is_valid():
            subject = postform.cleaned_data['boardsubject']
            name = postform.cleaned_data['boardname']
            gender = request.POST.get('boardgender',None)
            mail = postform.cleaned_data['boardmail']
            web = postform.cleaned_data['boardweb']
            content = postform.cleaned_data['boardcontent']
            unit = models.BoardUnit.object.create(bname=name,bgender =gender,bsubject=subject,bmail=mail,bweb=web,bcontent = content,bresponse = '')

            unit.save()
            message = 'saved...'
            postform = forms.PostForm()
            return redirect('/board/index/')
        else:
            message = 'validation error'
    else:
        message = 'tilte name content validation must input'
        postform = forms.PostForm()
    return render(request,'board/post.html',locals())

def board_login(request):
    message = ''
    if request.method =='POST':
        name = request.POST['username'].strip()
        password = request.POST['passwd']
        user1 = authenticate(username = name,password=password)
        if user1 is not None:
            if user1.is_active:
                auth.login(request,user1)
                return redirect('/board/adminmain/')
            else:
                message = 'account not authorize'
        else:
            message = 'login failed'
    return render(request,'login.html',locals())

def logout(request):
    auth.logout(request)
    return redirect('/board/index/')

def adminmain(request,pageindex = None):
    global page
    pagesize =3 
    boardall = models.BoardUnit.objects.all().oreder_by('-id')
    datasize = len(boardall)
    totpage = math.ceil(datasize/pagesize)
    if pageindex ==None:
        page = 0
        boardunits = models.BoardUnit.objects.order_by('-id')[:pagesize]
    elif pageindex == 'prev':
        start = (page-1)*pagesize
        if start>=0:
            boardunits = models.BoardUnit.objects.order_by('-id')[start:(start+pagesize)]
            page-=1
    elif pageindex == 'next':
        start = (page+1)*pagesize
        if start<datasize:
            boardunits = models.BoardUnit.objects.order_by('-id')[start:(start+pagesize)]
            page+=1
    elif pageindex =='ret':
        start = page*pagesize
        boardunits = models.BoardUnit.objects.order_by('-id')[start:(start+pagesize)]
        page += 1
    elif pageindex =='ret':
        start = page*pagesize
        boardunits = models.BoardUnit.objects.order_by('-id')[start(start+pagesize)]
    else:
        unit = models.BoardUnit.objects.get(id=pageindex)
        unit.bsubject = request.POST.get('boardsubject','')
        unit.bcontent = request.POST.get('boardcontent','')
        unit.bresponse = request.POST.get('boardresponse','')
        unit.save()
        return redirect('/board/adminmain/ret/')
    currentpage = page +1 
    return render(request,'board/adminmain.html',locals())

def delete(request,boardid = None , deletetype = None):
    unit = models.BoardUnit.objects.get(id=boardid)
    if deletetype == 'del':
        unit.delete()
        return redirect('/board/adminmain/')
    return render(request , 'board/delete.html',locals())
    