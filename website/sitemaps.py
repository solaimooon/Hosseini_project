from django.contrib import sitemaps
from django.urls import reverse


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 1
    changefreq = "daily"

    def items(self):
        return ["website:index" ,"website:masjed_emam_sajad","website:masjed_emam_sajad_live","website:masjed_emam_sajad_report"]

    def location(self, item):
        return reverse(item)
from django.contrib.sitemaps import Sitemap
from rezervation.models import *
class MosqueRezPageSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Mosque.objects.all()

    def location(self, obj):
        return reverse("website:rez_page", kwargs={"slug": obj.slug})