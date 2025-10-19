from django.http import HttpResponseNotFound
from django.template.response import TemplateResponse
from django.urls.resolvers import get_resolver
from urllib.parse import unquote


class DomainRouterMiddleware:
    """
    تشخیص دامنه و هدایت درخواست‌ها به اپ مناسب
    """

    def __init__(self, get_response):
        self.get_response = get_response
        self.website_urls = get_resolver('website.urls')
        self.rezervation_urls = get_resolver('rezervation.urls')
        self.profile_urls = get_resolver('my_profile.urls')

    def __call__(self, request):
        host = request.get_host().lower()
        path = request.path.lower()

        # مسیرهایی که نباید جدا بشن (admin, static, media)
        if path.startswith('/admin/') or path.startswith('/static/') or path.startswith('/media/'):
            return self.get_response(request)

        # مسیر پروفایل
        if path.startswith('/profile/'):
            resolver = self.profile_urls

        # سایت مسجد
        elif host in ['mjes.ir', 'www.mjes.ir']:
            resolver = self.website_urls

        # سایت رزرو
        elif host in ['kodom-masjed.com', 'www.kodom-masjed.com']:
            resolver = self.rezervation_urls

        else:
            return HttpResponseNotFound("دامنه ناشناخته است")

        try:
            # 🧩 رفع مشکل slugهای فارسی و فاصله‌دار
            path_info = unquote(request.path_info)

            # مسیریابی بر اساس دامنه انتخاب‌شده
            resolver_match = resolver.resolve(path_info)
            request.resolver_match = resolver_match

            # اجرای view
            response = resolver_match.func(request, *resolver_match.args, **resolver_match.kwargs)

            # ✅ در صورتی که خروجی TemplateResponse باشد، باید render شود
            if isinstance(response, TemplateResponse):
                response = response.render()

            return response

        except Exception as e:
            # در حالت دیباگ پیام دقیق را نمایش بده
            return HttpResponseNotFound(f"صفحه یافت نشد ({str(e)})")
