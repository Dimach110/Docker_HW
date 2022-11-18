from django.contrib import admin
from .models import Product, Stock, StockProduct


# Register your models here.

# class StockInline(admin.TabularInline):
#     model = Stock

class StockProductInline(admin.TabularInline):
    model = StockProduct

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']
    pass

@admin.register(Stock)
class Stock(admin.ModelAdmin):
    list_display = ['id']
    inlines = [StockProductInline,]
    pass