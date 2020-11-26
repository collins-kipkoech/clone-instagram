from django.shortcuts import render,get_object_or_404
from .models import Image


# Create your views here.
def home_view(request):
    posts = Image.objects.all()
    context = {
        'title':'home',
        'posts':posts,

    }
    return render(request,'instagram/home.html',context)

def image_details(request,pk):
    instance = get_object_or_404(Image,pk=pk)
    context = {
        'title':'details',
    }
    return render(request,'instagram/image_details.html')
