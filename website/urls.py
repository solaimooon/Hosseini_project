from django.urls import path
from .views import *
app_name='website'
urlpatterns = [
    path('', index ,name='index'),
    path('detail/', detail ,name=''),

]