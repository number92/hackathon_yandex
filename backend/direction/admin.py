from django.contrib import admin

from . import models


@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "level",
        "link",
        "duration",
        "price",
    )
    list_editable = (
        "link",
        "price",
    )
    list_filter = (
        "name",
        "level",
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
    list_filter = ("profession",)
    search_fields = ("profession",)


@admin.register(models.CoursesForProfession)
class CoursesForProfessionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "profession",
        "course",
    )
    list_editable = (
        "profession",
        "course",
    )
    list_filter = ("profession",)
    search_fields = ("profession",)
