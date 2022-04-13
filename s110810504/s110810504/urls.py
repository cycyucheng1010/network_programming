"""s110810504 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from ast import Delete
from django.contrib import admin
from django.urls import path
from CookieSessionApp.views import *
from hellodjango.views import *
from dice.views import *
from myapp.views import *
from login.views import *
from newsapp.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',hello_world),
    path('helloworld/<str:username>',hello_user),
    path('helloworld/<str:username>/time',hello_template),
    path('helloworld/<str:username>/time/static',hello_static),
    
    path('dice/test1',dice1),
    path('dice/test2',dice2),
    path('dice/test3/<str:username>',dice3),
    path('dice/show',show_list),
    path('show/',show),
    path('show2/',show_reverse),
    path('filter/',filter),  
    path('myapp/list_one/',list_one),
    path('myapp/list_all/',list_all),
    path('myapp/list_index/',list_index),
    path('myapp/post/',post),
    path('myapp/post1/',post1),
    path('myapp/postform/',postform),
    path('myapp/post2/',post2),
    path('myapp/delete/<int:id>/',delete),
    path('myapp/edit/<int:id>/',edit),
    path('myapp/edit/<int:id>/<str:mode>',edit),
    path('myapp/edit2/<int:id>/<str:mode>',edit2),

    path('CookieSessionApp/set_cookie/<str:key>/<str:value>',set_cookie),
    path('CookieSessionApp/set_cookie2/<str:key>/<str:value>',set_cookie2),
    path('CookieSessionApp/get_cookie/<str:key>/',get_cookie),
    path('CookieSessionApp/get_all_cookies/',get_all_cookies),
    path('CookieSessionApp/delete_cookie/<str:key>/',delete_cookie),
    path('CookieSessionApp/',CookieSessionApp_index),
    path('CookieSessionApp/index/',CookieSessionApp_index),
    path('CookieSessionApp/set_session/<str:key>/<str:value>',set_session),
    path('CookieSessionApp/get_session/<str:key>/',get_session),
    path('CookieSessionApp/get_all_sessions/',get_all_sessions),
    path('CookieSessionApp/vote/',vote),
    path('CookieSessionApp/set_sessions2/<str:key>/<str:value>/',set_session2),
    #path('CookieSessionApp/delete/session/<str:key>/',delete_session),
    path('CookieSessionApp/login/',login),
    path('CookieSessionApp/logout/',logout),
    path('login/adduser/',login_add_user),
    path('login/',login_index),
    path('login/index/',login_index),
    path('login/login/',login_login),
    path('login/logout/',login_logout),
    path('news/index/<str:pageindex>/',news_index),
    path('news/detail/<int:detailid>/',news_detail),
]
