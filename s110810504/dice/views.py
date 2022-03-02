from urllib import request
from django.shortcuts import render
import random
#dice1
def dice1(request):
    point = random.randint(1,6)
    return render(request,'dice1.html',locals())
#dice2
def dice2(request):
    point1 = random.randint(1,6)
    point2 = random.randint(1,6)
    point3 = random.randint(1,6)
    return render(request,'dice2.html',locals())
#dice3 global times
times =0
def dice3(request,username):
    global times
    times +=1
    #times +=1
    point = random.randint(1,6)
    #print('times=',times)
    dict1 = { 'point': point,'username':username,'times':times}
    return render(request,'dice3.html',dict1)
#show_list
def show_list(request):
    list1 = range(1,6)
    return render(request,'show.html',locals())
# show person data
def show(request):
    person1 = {'name':'A','phone':'123','age':1}
    person2 = {'name':'B','phone':'456','age':2}
    person3 = {'name':'C','phone':'789','age':3}
    persons = [person1,person2,person3]
    return render(request,'show2.html',locals())

# show person data reverse
def show_reverse(request):
    person1 = {'name':'A','phone':'123','age':1}
    person2 = {'name':'B','phone':'456','age':2}
    person3 = {'name':'C','phone':'789','age':3}
    persons = [person1,person2,person3]
    return render(request,'show3.html',locals())
def filter(request):
    value = 4 
    list1 = [1,2,3]
    pw='open the fucking door'

    html ='<h1>hello</h1>'
    value2 =False
    return render(request,'filter.html',locals())