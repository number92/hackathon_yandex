from django.contrib import admin

from . import models


@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "level",
        "description",
        "link",
        "status",
        "image",
        "duration",
        "price",
    )
    list_editable = (
        "name",
        "level",
        "description",
        "link",
        "status",
        "image",
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
        "courses_dir",
        "description",
        "link",
    )
    list_editable = (
        "name",
        "courses_dir",
        "description",
        "link",
    )
    list_filter = (
        "name",
        "link",
    )
    search_fields = (
        "name",
        "link",
    )


@admin.register(models.Profession)
class ProfessionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "short_name",
        "image",
        "description",
    )
    list_editable = (
        "name",
        "short_name",
        "image",
        "description",
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
