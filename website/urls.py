from django.urls import path
from .views import *

app_name = 'website'
urlpatterns = [
    path('', index, name='index'),
    path('rez/<str:slug>/', rez_page, name='rez_page'),
    # masjed pages
    path('m/jame_emam_sajjad/', masjed_emama_sajad, name='masjed_emam_sajad'),
    path('m/jame_emam_sajjad/live', masjed_emama_sajad_live, name='masjed_emam_sajad_live'),
    path('m/jame_emam_sajjad/report', masjed_emama_sajad_report, name='masjed_emam_sajad_report'),

    path("<str:category_slug>/", year_list, name="occasion_years"),
    path("<str:category_slug>/year:<int:year>/", occasion_list , name="occasion_list"),
    path("<str:category_slug>/<str:occasion_slug>/", night_list, name="night_list"),
    path("<str:category_slug>/<int:year>/<str:occasion_slug>/<str:night_slug>/", media_list,
         name="media_list"),
    path('archive/<str:media_slug>',media_single,name='single_media')

]
