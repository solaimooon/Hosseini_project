from django.urls import path
from .views import *
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from website.sitemaps import StaticViewSitemap
from .sitemaps import *
app_name = 'website'

sitemaps = {
    'static': StaticViewSitemap(),
}
urlpatterns = [

    path('', index, name='index'),
    path("detail", detail, name='detail'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

