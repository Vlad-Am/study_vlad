from django.contrib import admin

from .models import Study


@admin.register(Study)
class StudyAdmin(admin.ModelAdmin):
    list_display = ("name", "serial", "description",)
    list_filter = ("name", "serial")
