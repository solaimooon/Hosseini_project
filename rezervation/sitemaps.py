from django.contrib import sitemaps
from django.urls import reverse
from rezervation.models import *


# static page
class StaticViewSitemap(sitemaps.Sitemap):
    protocol = "https"
    domain = "kodom-masjed.com"

    priority = 1
    changefreq = "daily"

    def items(self):
        return ["reservation:index"]

    def location(self, item):
        return reverse(item)

    def get_urls(self, site=None, **kwargs):
        # دامنه را به‌صورت دستی تنظیم می‌کنیم
        from django.contrib.sites.models import Site
        site = Site(domain=self.domain, name=self.domain)
        return super().get_urls(site=site, **kwargs)



class MosqueRezPageSitemap(sitemaps.Sitemap):
    protocol = "https"
    domain = "kodom-masjed.com"  # 👈 دامنه مخصوص اپ مسجد

    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Mosque.objects.all()

    def location(self, obj):
        return reverse("reservation:detail", kwargs={"slug": obj.slug})