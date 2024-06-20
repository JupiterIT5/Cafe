from django.contrib import admin
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    pass

@admin.register(Supplies)
class SuppliesAdmin(admin.ModelAdmin):
    pass

@admin.register(PositionSupplies)
class Position_suppliesAdmin(admin.ModelAdmin):
    pass

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass

@admin.register(PositionOrder)
class Position_orderAdmin(admin.ModelAdmin):
    pass

@admin.register(Сharacteristic)
class СharacteristicAdmin(admin.ModelAdmin):
    pass

@admin.register(FullCharacteristic)
class FullCharacteristicAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price', 'exists')
    list_display_links = ('name',)
    list_editable = ('price', 'exists')
    search_fields = ('name', 'price')
    list_filter = ('exists',)
    
@admin.register(WareHouse)
class WareHouseAdmin(admin.ModelAdmin):
    pass
 
@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    pass
    
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass