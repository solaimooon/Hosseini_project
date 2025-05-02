from django.shortcuts import render

def index (request):
    return render(request,'slider-home.html')

def detail (request):
    return render(request, 'media-tabs.html')



# Create your views here.
