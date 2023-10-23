from django.contrib import admin

from .models import *


@admin.register(MainFaq)
class MainFaqAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    search_fields = ['id', 'title', 'text']


@admin.register(PricingFaq)
class PricingFaqAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    search_fields = ['id', 'title', 'text']


@admin.register(HelpRequest)
class HelpRequestAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'email']
    list_display_links = ['id', 'email']
    search_fields = ['id', 'status', 'email']
    list_filter = ['status', 'email']
