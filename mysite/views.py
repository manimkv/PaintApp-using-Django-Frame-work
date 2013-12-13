from django.http import HttpResponse
import datetime
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from paintapp.models import Image

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def paint(request):
    return render(request, 'paint.html')

@csrf_exempt
def save(request):
    picname=request.POST.get('name')
    picdata=request.POST.get('data')
    p=Image.objects.create(name=picname,data=picdata)
    return render(request, 'paint.html')

def gallery(request):
    posts=[dict(id=i.id,title=i.name) for i in Image.objects.order_by('id')]
    return render(request, 'gallery.html', {'posts': posts})

def load(request,imgname):
    data=Image.objects.filter(name=imgname)
    print data[0].id
    for i in Image.objects.filter(name=imgname):
        print i.id
    posts=[dict(id=i.id,title=i.name,imagedata=i.data) for i in Image.objects.filter(name=imgname)]
    return render(request,'imageload.html',{'posts':posts})

def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'datetime': now})

