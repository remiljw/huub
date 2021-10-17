from django.contrib import admin
from .models import Product, Brand, Order, Delivery, DeliveredItem, OrderItem
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    search_fields = ['__all__']
    list_display = ['name', 'price']

class BrandAdmin(admin.ModelAdmin):
    search_fields = ['__all__']
    list_display = ['name']

class OrderAdmin(admin.ModelAdmin):
    search_fields = ['__all__']
    list_display = ['customer_name', 'brand', 'reference', 'price_total', 'order_date']
    list_filter = ['brand__name']

class OrderItemAdmin(admin.ModelAdmin):
    search_fields = ['__all__']
    list_display = ['product', 'quantity', 'price']

class DeliveryAdmin(admin.ModelAdmin):
    search_fields = ['__all__']
    list_display = ['order', 'shipped', 'created_at', 'updated_at']
    list_filter = ['shipped']

class DeliveredItemAdmin(admin.ModelAdmin):
    search_fields = ['__all__']
    list_display = ['product_name', 'quantity', 'created_at', 'updated_at']



admin.site.register(Product, ProductAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Delivery, DeliveryAdmin)
admin.site.register(DeliveredItem, DeliveredItemAdmin)