from django.contrib import admin
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_filter = ('is_exists',)

@admin.register(Supply)
class SupplyAdmin(admin.ModelAdmin):
    pass

@admin.register(PosSupply)
class PosSupplyAdmin(admin.ModelAdmin):
    pass

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass

@admin.register(PosOrder)
class PosOrderAdmin(admin.ModelAdmin):
    pass

@admin.register(Parametr)
class ParametrAdmin(admin.ModelAdmin):
    pass

@admin.register(PosParametr)
class PosParametrAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price', 'is_exists')
    list_display_links = ('name',)
    list_editable = ('price', 'is_exists')
    search_fields = ('name', 'price')
    list_filter = ('is_exists',)
    
@admin.register(WareHouse)
class WareHouseAdmin(admin.ModelAdmin):
    pass
 
@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    pass
    
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass