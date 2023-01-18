from django.contrib import admin

from . import models


@admin.register(models.Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "created_at",
        "name",
        "description",
        "type",
        "framework",
        "domain_name",
        "user",
    )
    list_filter = ("type", "framework", "user")


@admin.register(models.Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at", "name", "description", "price")
