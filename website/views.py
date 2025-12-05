from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from .models import *
from rezervation import *



def index(request):
    mosques = Mosque.objects.all()
    return render(request, 'slider-home.html', {"mosques": mosques})


def detail(request,):
    mosque = Mosque.objects.all()[0]
    return render(request, 'media-tabs.html', {"mosque": mosque})


def my_reservation_oprator_view (request):
    return render(request, 'reservation_operator.html')