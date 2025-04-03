from django.contrib import admin
from .models import Supplier, Product


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'city', 'supplier', 'debt', 'level')
    list_filter = ('city',)
    search_fields = ('name',)
    actions = ['clear_debt']

    def clear_debt(self, request, queryset):
        queryset.update(debt=0.00)
    clear_debt.short_description = "Очистить задолженность"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date', 'supplier')
