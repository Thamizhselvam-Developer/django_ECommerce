from django.contrib import admin
from .models import Products, Category

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ["productName", "productImageLink", "productPrice", "category"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["categoryName"]