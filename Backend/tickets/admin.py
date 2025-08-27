from django.contrib import admin
from .models import Ticket


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "priority",
        "status",
        "sector",
        "created_by",
        "assigned_to",
        "updated_by",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "priority",
        "status",
        "sector",
        "created_at",
        "updated_at",
    )
    search_fields = ("title", "description", "created_by__username", "assigned_to__username")
    autocomplete_fields = ("created_by", "assigned_to", "updated_by")
    readonly_fields = ("created_at", "updated_at")
    ordering = ("-created_at",)


