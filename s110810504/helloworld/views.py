from django.shortcuts import render
from django.http import HttpResponse
#test1
def hello_user(request,username):
    return HttpResponse('hello '+ username)

# test2
def hello_user(request,username):
    return HttpResponse('hello '+ username)

