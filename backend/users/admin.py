from django.contrib import admin

from . import models


class CourseInline(admin.TabularInline):
    model = models.UserCourses

    readonly_fields = ("user",)


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "username",
        "email",
        "is_active",
    )
    save_on_top = True

    list_editable = ("email", "is_active")
    list_filter = ("email",)
    inlines = (CourseInline,)
    search_fields = (
        "id",
        "email",
    )


@admin.register(models.UserCourses)
class UserCoursesAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "course", "status")
    list_editable = ("user", "course", "status")
    list_filter = ("id",)


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

    search_fields = ("user",)
