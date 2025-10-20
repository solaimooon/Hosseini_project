from django.contrib import sitemaps
from django.urls import reverse
from rezervation.models import *


# static page
class StaticViewSitemap(sitemaps.Sitemap):


    priority = 1
    changefreq = "daily"

    def items(self):
        return ["reservation:index"]

    def location(self, item):
        return reverse(item)





class MosqueRezPageSitemap(sitemaps.Sitemap):


    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Mosque.objects.all()

    def location(self, obj):
        return reverse("reservation:detail", kwargs={"slug": obj.slug})