from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = My_user
        fields = ("phone_number",)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = My_user
        fields = ("phone_number", "role", "is_active", "is_staff", "is_superuser")

@admin.register(My_user)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = My_user
    list_display = ("phone_number", "role", "is_staff", "is_active")
    list_filter = ("role", "is_staff", "is_active")

    fieldsets = (
        (None, {"fields": ("phone_number", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
        ("Role info", {"fields": ("role",)}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("phone_number", "password1", "password2", "is_staff", "is_active", "role"),
        }),
    )
    search_fields = ("phone_number",)
    ordering = ("phone_number",)


admin.site.register(Mosque_operator)