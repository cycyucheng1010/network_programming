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
from django.contrib import admin
from django.urls import path
from hellodjango.views import *
from dice.views import *
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
]
