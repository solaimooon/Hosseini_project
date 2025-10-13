from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from website.sitemaps import StaticViewSitemap, MosqueRezPageSitemap
from django.conf import settings
from django.conf.urls.static import static
from .view import domain_index

sitemaps = {
    "static": StaticViewSitemap,
    'mosques': MosqueRezPageSitemap(),
}

urlpatterns = [

                  path('admin/', admin.site.urls),
                  path('', domain_index, name="domain_index"),
                  path('profile/', include('my_profile.urls')),
                  path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
                  path('robots.txt', include('robots.urls')),
                  path('', include(('website.urls', 'website'), namespace='website')),  # REGISTER namespace
                  path('', include(('rezervation.urls', 'rezervation'), namespace='rezervation')),  # REGISTER namespace
                  path('profile/', include('my_profile.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
