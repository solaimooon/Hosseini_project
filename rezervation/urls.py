from django.urls import path
from .views import *
app_name='reservation'
urlpatterns = [
    path('my_reservation_oprator/',my_reservation_oprator_view,name='my_reservation_oprator')
]