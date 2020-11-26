from django.shortcuts import render
from .models import Image


# Create your views here.
def home_view(request):
    posts = Image.objects.all()
    context = {
        'title':'home',
        'posts':posts,

    }
    return render(request,'instagram/home.html',context)

def image_details(request):
    context = {
        'title':'details',
    }
    return render(request,'instagram/image_details.html')
