from django.shortcuts import get_object_or_404, render
from rezervation.models import *
def index (request):
    mosques=Mosque.objects.all()
    return render(request,'slider-home.html',{"mosques":mosques})

def rez_page (request,slug):
    mosque = get_object_or_404(Mosque, slug=slug)[0]
    return render(request, 'media-tabs.html',{"mosque":mosque})



# Create your views here.
