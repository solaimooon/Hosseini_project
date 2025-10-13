from django.urls import include, path, re_path
from django.http import HttpResponseNotFound
from django.urls.resolvers import get_resolver

class DomainRouterMiddleware:
    """
    تشخیص دامنه و هدایت درخواست‌ها به اپ مناسب
    """

    def __init__(self, get_response):
        self.get_response = get_response

        # رزولورهای جدا برای هر دامنه
        self.website_urls = get_resolver('website.urls')
        self.rezervation_urls = get_resolver('rezervation.urls')
        self.profile_urls = get_resolver('my_profile.urls')

    def __call__(self, request):
        host = request.get_host().lower()

        # مسیر اپ مشترک پروفایل
        if request.path.startswith('/profile/'):
            resolver = self.profile_urls

        # سایت مسجد (mjes.ir)
        elif host in ['mjes.ir', 'www.mjes.ir']:
            resolver = self.website_urls

        # سایت اصلی (kodom-masjed.com)
        elif host in ['kodom-masjed.com', 'www.kodom-masjed.com']:
            resolver = self.rezervation_urls

        else:
            return HttpResponseNotFound("دامنه ناشناخته است")

        # رزولوشن دستی مسیر
        resolver_match = resolver.resolve(request.path_info)
        request.resolver_match = resolver_match
        return resolver_match.func(request, *resolver_match.args, **resolver_match.kwargs)
