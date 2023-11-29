from django.contrib import admin

from . import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "id",
        "email",
        "password",
        "first_name",
        "last_name",
    )
    list_editable = ("password", "email")
    list_filter = ("username", "email")
    search_fields = ("username", "email")
