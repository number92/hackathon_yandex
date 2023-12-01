from django.contrib import admin

from . import models


@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "level",
        "description",
        "link",
        "progress",
    )
    list_editable = (
        "name",
        "level",
        "description",
        "link",
        "progress",
    )
    list_filter = ("name", "level")
    search_fields = ("name",)
