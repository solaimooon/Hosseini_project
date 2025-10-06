from django.urls import path
from .views import *

app_name = 'website'
urlpatterns = [
    path('',index, name='index'),
    # masjed pages

    path('live',live, name='live'),
    path('report',report, name='report'),

    path("<str:category_slug>/", year_list, name="occasion_years"),
    path("<str:category_slug>/year:<int:year>/", occasion_list , name="occasion_list"),
    path("<str:category_slug>/<str:occasion_slug>/", night_list, name="night_list"),
    path("<str:category_slug>/<int:year>/<str:occasion_slug>/<str:night_slug>/", media_list,
         name="media_list"),
    path('archive/<str:media_slug>',media_single,name='single_media')

]
