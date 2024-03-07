from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin

from crew.models import Director, Actor


@admin.register(Director)
class DirectorAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("birthday", "photo", "country")
    fieldsets = UserAdmin.fieldsets + (
        (
            "Additional info",
            {
                "fields": ("birthday", "photo", "country"),
            },
        ),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "birthday",
                        "photo",
                        "country",
                    )
                },
            ),
        )
    )


@admin.register(Actor)
class ActorAdmin(ModelAdmin):
    list_display = [
        "first_name",
        "last_name",
        "birthday",
        "photo",
        "country",
    ]
    list_filter = [
        "birthday",
        "country",
    ]
    search_fields = [
        "first_name",
        "last_name",
    ]
