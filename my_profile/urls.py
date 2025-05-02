from django.urls import path
from .views import *

app_name = 'my_profile'
urlpatterns = [
    path('Register/', Register_view, name='Register'),
    path('Authentication/', Authentication, name='Authentication'),
    path('login/', log_in_view, name='log_in'),
    path('logout/', log_out_view, name='log_out'),
    path('profile/',profile_view , name='profile'),

]
