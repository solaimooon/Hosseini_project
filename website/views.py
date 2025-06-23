from django.shortcuts import get_object_or_404, render
from rezervation.models import *
def index (request):
    mosques=Mosque.objects.all()
    return render(request,'slider-home.html',{"mosques":mosques})

def rez_page (request,slug):
    mosque = get_object_or_404(Mosque, slug=slug)
    return render(request, 'media-tabs.html',{"mosque":mosque})

def masjed_emama_sajad(request):
    return render(request,'masjed_template.html')


def masjed_emama_sajad_live(request):
    return render(request, 'live.html')

def masjed_emama_sajad_report(request):
    return render(request, 'report.html')

# Create your views here.
