from django.contrib import admin

from .models import *


@admin.register(MainFaq)
class MainFaqAdmin(admin.ModelAdmin):
    pass


@admin.register(PricingFaq)
class PricingFaqAdmin(admin.ModelAdmin):
    pass
