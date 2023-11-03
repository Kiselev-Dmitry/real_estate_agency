from django.contrib import admin

from .models import Flat, Complaint, Owner


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ("town", "address", "owner")
    readonly_fields = ("created_at",)
    list_display = ("address", "price", "new_building", "construction_year", "town",)
    list_editable = ("new_building",)
    list_filter = ("new_building",)
    raw_id_fields = ("liked_by",)

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ("flats_in_property",)
    exclude = ("flats_in_property",)

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ("user", "flat",)

# admin.site.register(Flat, FlatAdmin)
