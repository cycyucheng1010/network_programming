from email import message
from django.shortcuts import redirect, render
from myapp.models import student
from myapp.forms import PostForm
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
def post(request):
    if request.method == "POST":
        print('POST')
        mess = request.POST['username']
    else:
        print('GET')
        mess = '表單資料尚未送出'
    return render(request,'myapp/post.html',locals())
def post1(request):
    if request.method == 'POST':
        Name = request.POST['Name']
        Sex = request.POST['Sex']
        Birth = request.POST['Birth']
        Email = request.POST['Email']
        Phone = request.POST['Phone']
        Home_Address = request.POST['Home_Address']
        unit = student.objects.create(Name = Name, Sex = Sex , Birth = Birth, Email=Email ,Phone = Phone , Home_Address = Home_Address )
        unit.save()
        return redirect('/myapp/list_index/')
    else:
        message = '請輸入資料(資料不做驗證)'
    return render(request,'myapp/post1.html',locals())
def postform(request):
    postform = PostForm()
    return render(request,'myapp/postform.html',locals())
def post2(request):
    if request.method == 'POST':
        postform =PostForm(request.POST)
        if postform.is_valid():
            Name = postform.cleaned_data['Name']
            Sex = postform.cleaned_data['Sex']
            Birth = postform.cleaned_data['Birth']
            Email = postform.cleaned_data['Email']
            Phone = postform.cleaned_data['Phone']
            Home_Address = request.POST['Home_Address']
            unit = student.objects.create(Name = Name, Sex = Sex , Birth = Birth, Email=Email ,Phone = Phone , Home_Address = Home_Address )
            unit.save()
            message = 'already saved'
            return redirect('/myapp/list_index/')
        else:
            message = 'validation error'
    else: 
        message = 'name sex birth must entry'
        postform = PostForm()
    return render(request,'myapp/post2.html',locals())

def delete(request,id=None):
    if id != None:
        if request.method =='POST':
            id  = request.POST['Id']
        try: 
            unit = student.objects.get(id=id)
            unit.delete()
            return redirect('/myapp/list_index/')
        except:
            message = 'loading error'
    return render(request,'myapp/delete.html',locals())