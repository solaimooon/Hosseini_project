from django.contrib import admin
from .models import Mosque, Hall, HallImage, Facility


class HallImageInline(admin.TabularInline):
    model = HallImage
    extra = 1  # تعداد فرم‌های خالی برای افزودن تصویر جدید
    fields = ('image', 'caption')
    readonly_fields = ()
    show_change_link = True


class HallInline(admin.StackedInline):
    model = Hall
    extra = 1
    fields = ('name', 'capacity', 'is_active', 'video_file', 'price', 'facilities')
    filter_horizontal = ('facilities',)
    show_change_link = True
    inlines = [HallImageInline]  # این کار به صورت مستقیم مجاز نیست، اما در پایین راه‌حل توضیح داده شده


# از آنجایی که نمی‌توان مستقیماً Inline در Inline داشت، تصاویر سالن را داخل admin جداگانه اضافه می‌کنیم
class HallAdmin(admin.ModelAdmin):
    list_display = ('name', 'mosque', 'capacity', 'is_active', 'price')
    list_filter = ('is_active', 'mosque')
    search_fields = ('name',)
    filter_horizontal = ('facilities',)
    inlines = [HallImageInline]


class MosqueAdmin(admin.ModelAdmin):
    list_display = ('name', 'rigen', 'address')
    filter_horizontal = ('facilities',)
    inlines = [HallInline]


class FacilityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class HallImageAdmin(admin.ModelAdmin):
    list_display = ('hall', 'caption')
    search_fields = ('caption', 'hall__name')


# ثبت همه مدل‌ها
admin.site.register(Mosque, MosqueAdmin)
admin.site.register(Hall, HallAdmin)
admin.site.register(HallImage, HallImageAdmin)
admin.site.register(Facility, FacilityAdmin)
