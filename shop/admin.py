from django.contrib import admin
from .models import GenericCategory, GenericValues, Product, ProductFilter, Category
# Register your models here.


class GenericValuesInline(admin.TabularInline):
    model = GenericValues
    extra = 1

@admin.register(GenericCategory)
class GenericCategoryAdmin(admin.ModelAdmin):
    inlines = [GenericValuesInline]
    list_display = ['name']
    list_per_page = 20


class ProductFilterInline(admin.TabularInline):
    model = ProductFilter
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductFilterInline]
    list_display = ['name']
    list_per_page = 20


admin.site.register(Category)