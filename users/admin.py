from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "phone_number", "avatar", "country")
    list_filter = ("country",)
    search_fields = ("email",)
