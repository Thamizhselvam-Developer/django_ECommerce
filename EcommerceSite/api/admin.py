from django.contrib import admin
from .models import Products,Category
# Register your models here.
@admin.register(Products)
class Products(admin.ModelAdmin):
    list_display=["id","productName"]
    search_fields = ('name',) 
    
@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display=["id","categoryName"]