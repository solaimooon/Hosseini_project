from django.urls import path
from .views import *
app_name='reservation'
urlpatterns = [

    path('', index, name='index'),
    path('rez/<str:slug>/', rez_page, name='rez_page'),
    path('my_reservation_oprator/',my_reservation_oprator_view,name='my_reservation_oprator')
]