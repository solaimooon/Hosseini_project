from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap

urlpatterns = [
                  path('admin/', admin.site.urls),  # ✅ مسیر پنل مدیریت اضافه شد
                  path('', include(('rezervation.urls', 'rezervation'), namespace='rezervation')),

                  # اپ‌ها
                  path('profile/', include('my_profile.urls')),
                  path('robots.txt', include('robots.urls')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
