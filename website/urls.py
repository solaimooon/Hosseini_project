from django.urls import path
from .views import *
app_name='website'
urlpatterns = [
    path('', index ,name='index'),
    path('rez/<str:slug>/', rez_page ,name='rez_page'),

]