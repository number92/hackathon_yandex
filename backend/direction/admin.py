from django.contrib import admin

from . import models


@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "level",
        "link",
        "status",
        "direction",
        "duration",
        "price",
    )
    list_editable = (
        "name",
        "level",
        "link",
        "status",
        "direction",
        "duration",
        "price",
    )
    list_filter = (
        "name",
        "level",
        "status",
    )
    search_fields = (
        "name",
        "link",
    )


@admin.register(models.Direction)
class DirectionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )
    list_editable = ("name",)
    list_filter = ("name",)
    search_fields = ("name",)


@admin.register(models.Profession)
class ProfessionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "short_name",
    )
    list_editable = (
        "name",
        "short_name",
    )
    list_filter = (
        "name",
        "short_name",
    )
    search_fields = ("name",)


@admin.register(models.ProfessionInDirection)
class ProfessionInDirectionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "__str__",
        "profession",
        "direction",
    )
    list_editable = (
        "profession",
        "direction",
    )
