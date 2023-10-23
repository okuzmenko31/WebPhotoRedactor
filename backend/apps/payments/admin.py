from django.contrib import admin

from .models import Plan, Order, ForeignOrder


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Main info', {'fields': ('name', 'price', 'description')}),
        ('Credits count', {'fields': (
            'up_scales_count',
            'bg_deletions_count',
            'jpg_artifacts_deletions_count',
        )})
    )
    list_display = ['id', 'name', 'price']
    list_display_links = ['id', 'name']
    search_fields = ['id', 'name', 'price']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Main info', {'fields': (
            'user',
            'plan',
            'status',
            'payment_service'
        )}
        ),
    )
    list_display = ['id', 'user', 'plan', 'status', 'payment_service']
    list_editable = ['user', 'plan', 'status', 'payment_service']
    list_display_links = ['id']
    list_filter = ['user', 'plan', 'status']
    search_fields = ['id', 'user', 'plan', 'status', 'payment_service']
