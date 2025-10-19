from django.urls import path
from .views import *
from rezervation.sitemaps import StaticViewSitemap
from django.contrib.sitemaps.views import sitemap
from .sitemaps import *
app_name='reservation'

sitemaps = {
    'static': StaticViewSitemap(),
    'mosques': MosqueRezPageSitemap(),

}
urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('', index, name='index'),
    path('rez/<str:slug>/', detail, name='detail'),
    path('my_reservation_oprator/',my_reservation_oprator_view,name='my_reservation_oprator')
]


