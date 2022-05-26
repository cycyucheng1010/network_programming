from django.shortcuts import render, redirect
from albumapp import models
from django.contrib.auth import authenticate
from django.contrib import auth
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os


# Create your views here.

def index(request):
    albums = models.AlbumModel.objects.all().order_by('-id')
    totalalbum = len(albums)
    photos = []
    lengths = []
    for album in albums:
        photo = models.PhotoModel.objects.filter(palbm__atitle = album.atitle).order_by('-id')

        lengths.append(len(photo))
        if len(photo) == 0:
            photos.append('')

        else:
            photos.append(photo[0].purl)
    
    return render(request, 'index.html', locals())

def albumshow(request, albumid = None):
    album = albumid
    photos = models.PhotoModel.objects.filter(palbm__atitle = album.atitle).order_by('-id')
    monophoto = photos[0]
    totalphoto = len(photos)
    return render(request, 'albumshow.html', locals())

def albumphoto(request, photoid = None, albumid = None):
    album = albumid
    photo = models.PhotoModel.objects.get(id = photoid)
    photo.phit += 1
    photo.save()
    return render(request, 'albumphoto.html', locals())

def login(request):
    message = ''
    if request.method == 'POST':
        name = request.POST['username'].strip()
        password = request.POST['password']
        user1 = authenticate(username = name , password = password)

        if user1 is not None:
            if user1.is_active:
                auth.login(request, user1)
                return redirect('/adminmain/')

            else:
                message = '帳號尚未啟用'

        else:
            message = '登入失敗'

    return render(request, 'login.html', locals())

def logout(request):
    auth.logout(request)
    return redirect('/index/')

def adminmain(request, albumid = None):
    if albumid == None:
        albums = models.AlbumModel.objects.all().order_by('-id')
        totalalbum = len(albums)
        photos = []
        lengths = []
        for album in albums:
            photo = models.PhotoModel.objects.filter(palbum__atitle = album.atitle).order_by('-id')
            lengths.append(len(photo))

            if len(photo) == 0:
                photos.append('')

            else:
                photos.append(photo[0].purl)
    else:
        album = models.AlbumModel.objects.get(id = albumid)
        photo = models.PhotoModel.objects.filter(palbum__atitle = album.atitle).order_by('-id')

        for photounit in photo:
            os.remove(os.path.join(settings.MEDIA_ROOT, photounit.purl))

        album.delete()
        return redirect('adminmain')

    return render(request, 'adminmain.html', locals())

def adminadd(request):
    message = ''
    title = request.POST.get('album_title', '')
    location = request.POST.get('album_location', '')
    desc = request.POST.get('album_desc', '')

    if title == '':
        message = '相簿名稱一定要填寫'
    else:
        unit = models.AlbumModel.objects.create(atitle = title, alocation = location, adesc = desc)
        unit.save()
        return redirect('/adminmain/')
    
    return render(request, 'adminadd.html', locals())

def adminfix (request, albumid = None, photoid = None, deletetype = None):
    album = models.AlbumModel.objects.get(id = albumid)
    photos = models.PhotoModel.objects.filter(palbum__atitle = albumid).order_by('-id')
    totalphoto = len(photos)

    if photoid != None:
        if photoid == 999999:
            album.atitle = request.POST.get('album_title', '')
            album.alocation = request.POST.get('album_location', '')
            album.adesc = request.POST.get('album_desc', '')
            album.save()
            files = []
            descs = []
            picurl = ['ap_picurl1', 'ap_picurl2', 'ap_picurl3', 'ap_picurl4', 'ap_picurl5']
            subject = ['ap_subject1', 'ap_subject2', 'ap_subject3', 'ap_subject4', 'ap_subject5']

            for count in range(0, 5):
                files.append(request.FILES.get(picurl[count], ''))
                descs.append(request.POST.get(subject[count], ''))
            
            i = 0
            for upfile in files:
                if upfile != '' and descs[i] != '':
                    fs = FileSystemStorage()
                    filename = fs,save(upfile.name, upfile)
                    unit = models.PhotoModel.objects.create(palbum = album, psubject = descs[i], purl = upfile)
                    unit.save()
                    i += 1

                return redirect('/adminfix/' + str(album.id) + '/')
            
        elif deletetype == 'update':
            photo = models.PhotoModel.objects.get(id = photoid)
            photo.psubject = request.POST.get('ap_subject', '')
            photo.save()
            return redirect('/adminfix/' + str(album.id) + '/')
        
        elif deletetype == 'delete':
            photo = models.PhotoModel.objects.get(id = photoid)
            os.remove(os.path.join(settings.MEDIA_ROOT, photo.purl))
            photo.delete()
            return redirect('/adminfix/' + str(album.id) + '/')
    return render(request, 'adminfix.html', locals())