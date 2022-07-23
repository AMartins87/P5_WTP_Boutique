from django.contrib import admin
from .models import Product, Category

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    """Tells admin which fields to display """
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )
    
    """Sorts the products by SKU using the ordering attribute """
    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)