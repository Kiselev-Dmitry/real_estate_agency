from django.contrib import admin

from .models import Flat, Complaint, Owner


class OwnershipInline(admin.TabularInline):
    model = Owner.flats_in_property.through
    raw_id_fields = ("owner", "flat",)


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ("town", "address", "owner")
    readonly_fields = ("created_at",)
    list_display = ("address", "price", "new_building", "construction_year", "town",)
    list_editable = ("new_building",)
    list_filter = ("new_building",)
    raw_id_fields = ("liked_by",)
    inlines = [OwnershipInline]


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ("flats_in_property",)
    inlines = [OwnershipInline]
    exclude = ("flats_in_property",)


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ("user", "flat",)
