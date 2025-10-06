from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from .models import *


def index(request):
    mosques = Mosque.objects.all()
    return render(request, 'slider-home.html', {"mosques": mosques})


def rez_page(request, slug):
    mosque = get_object_or_404(Mosque, slug=slug)
    return render(request, 'media-tabs.html', {"mosque": mosque})


def my_reservation_oprator_view (request):
    return render(request, 'reservation_operator.html')
# Create your views here.
