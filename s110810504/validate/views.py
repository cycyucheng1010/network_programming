from multiprocessing import AuthenticationError
from django.shortcuts import redirect, render
from validate import forms
#from validate.forms import PostForm
from django.contrib.auth import authenticate
from django.contrib import auth
# Create your views here.
def vali_index(request):
    if request.method == "POST":
        postform = forms.PostForm(request.POST)
        if postform.is_valid():
            username = postform.cleaned_data['username']
            pd = postform.cleaned_data['pd']
            user1 = authenticate(username=username,password=pd)
            if user1 is not None:
                auth.login(request,user1)
                postform =forms.PostForm()
                return redirect('/validate/manage/')
            else:
                message = 'login failed'
        else:
            message = 'valitation code error'
    else:
        message = 'account password validation code must input'
        postform =  forms.PostForm()
    return render(request,'validate/index.html',locals())

def vali_manage(request):
    return render(request,'validate/manage.html',locals())