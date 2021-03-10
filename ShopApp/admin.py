from django.contrib import admin
from .models import Product_category, Product

# Register your models here.

class ProductCategoryAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")

class ProductAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")

admin.site.register(Product_category, ProductCategoryAdmin)

admin.site.register(Product, ProductAdmin)
