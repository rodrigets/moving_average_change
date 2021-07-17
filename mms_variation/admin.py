from django.contrib import admin
from .models import MmsVariation


class MmsVariationAdmin(admin.ModelAdmin):
    list_display = ("id", "pair", "timestamp", "mms_20", "mms_50", "mms_200")
    list_display_links = ("id", "pair")
    search_fields = ("id", "pair", "timestamp")
    list_per_page = 25


# Register your models here.
admin.site.register(MmsVariation, MmsVariationAdmin)
