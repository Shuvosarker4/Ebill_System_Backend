from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'wifi_plan', 'connection_type', 'is_active')
    list_filter = ('wifi_plan', 'connection_type', 'is_active')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number')
