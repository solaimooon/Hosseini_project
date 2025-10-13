from django.shortcuts import redirect

import rezervation.views
import website
import rezervation

from django.http import HttpResponse

def domain_index(request):
    return HttpResponse("در حال تشخیص دامنه و هدایت به اپ مربوطه ...")
# def domain_index(request):
#     host = request.META.get("HTTP_HOST", "")
#
#     if host in ["mjes.ir", "www.mjes.ir"]:
#         return website.views.index(request)   # صفحه اصلی مسجد
#     elif host in ["kodom-masjed.com", "www.kodom-masjed.com"]:
#         return rezervation.views.index(request)   # صفحه اصلی رزرو
#     else:
#         return redirect("rezervation:index")   # پیش‌فرض
