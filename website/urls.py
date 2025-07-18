from django.urls import path
from .views import *

app_name = 'website'
urlpatterns = [
    path('', index, name='index'),
    path('rez/<str:slug>/', rez_page, name='rez_page'),
    path('m/jame_emam_sajjad/', masjed_emama_sajad, name='masjed_emam_sajad'),
path('m/jame_emam_sajjad/live', masjed_emama_sajad_live, name='masjed_emam_sajad_live'),
path('m/jame_emam_sajjad/report', masjed_emama_sajad_report, name='masjed_emam_sajad_report'),


]
