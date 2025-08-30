from django.contrib import admin
from .models import Category, Occasion, Night, MediaFile,owner,style_media_file
from my_profile.models import Mosque_operator


class MosqueFilteredAdmin(admin.ModelAdmin):
    """
    کلاس پایه برای فیلتر کردن داده‌ها بر اساس مسجد اوپراتور
    """
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs

        # بررسی اینکه کاربر اوپراتور مسجد هست
        if hasattr(request.user, "mosque_operator"):
            user_mosque = request.user.mosque_operator.mosque
            if self.model == Category:
                return qs.filter(mosque=user_mosque)
            elif self.model == Occasion:
                return qs.filter(category__mosque=user_mosque)
            elif self.model == Night:
                return qs.filter(occasion__category__mosque=user_mosque)
            elif self.model == MediaFile:
                return qs.filter(night__occasion__category__mosque=user_mosque)

        return qs.none()

    def save_model(self, request, obj, form, change):
        """
        اطمینان از ست شدن درست مسجد برای اوپراتورها
        """
        if not request.user.is_superuser and hasattr(request.user, "mosque_operator"):
            user_mosque = request.user.mosque_operator.mosque
            if isinstance(obj, Category):
                obj.mosque = user_mosque
            elif isinstance(obj, Occasion) and not obj.category_id:
                # اگر می‌خواهید دسته‌بندی به‌طور خودکار ست شود
                obj.category.mosque = user_mosque
            elif isinstance(obj, Night) and not obj.occasion_id:
                obj.occasion.category.mosque = user_mosque
            elif isinstance(obj, MediaFile) and not obj.night_id:
                obj.night.occasion.category.mosque = user_mosque

        super().save_model(request, obj, form, change)


@admin.register(Category)
class CategoryAdmin(MosqueFilteredAdmin):
    list_display = ("name", "mosque")
    search_fields = ("name", "mosque__name")


@admin.register(Occasion)
class OccasionAdmin(MosqueFilteredAdmin):
    list_display = ("name", "year", "category")
    search_fields = ("name", "year", "category__name")


@admin.register(Night)
class NightAdmin(MosqueFilteredAdmin):
    list_display = ("number", "occasion")
    search_fields = ("occasion__name",)


@admin.register(MediaFile)
class MediaFileAdmin(MosqueFilteredAdmin):
    list_display = ("title", "media_type", "night")
    search_fields = ("title", "media_type")
    list_filter = ("media_type",)

admin.site.register(style_media_file)
admin.site.register(owner)