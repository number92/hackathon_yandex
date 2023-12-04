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


@admin.register(models.UserGradeMap)
class UserGradeMapAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "start_level",
        "end_level",
        "start_prof",
        "end_prof",
        "data_joined",
    )
    list_editable = ("start_level", "end_level", "start_prof", "end_prof")
    list_filter = ("id", "user")
    search_fields = ("user",)
