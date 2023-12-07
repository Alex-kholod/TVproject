from django.contrib import admin
from .models import *


@admin.register(Supply)
class SupplyAdmin(admin.ModelAdmin):
    list_display = ('date', 'tv', 'supplier', 'staff', 'count')
    list_filter = ('staff', 'date')
    search_fields = ('tv__tv_model', 'count')
    readonly_fields = ('date',)


@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ('date', 'tv', 'distributor', 'staff', 'count', 'car', 'storehouse')
    list_filter = ('staff', 'date')
    search_fields = ('tv__tv_model', 'count')
    readonly_fields = ('date',)


@admin.register(Stocks)
class StocksAdmin(admin.ModelAdmin):
    list_display = ('tv', 'storehouse', 'stock_count')
    list_filter = ('storehouse',)
    search_fields = ('tv__tv_model', 'stock_count')


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'email', 'phone')
    search_fields = ('name', 'email')


@admin.register(Distributor)
class DistributorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone')
    search_fields = ('full_name', 'email')


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('car_name', 'capacity')
    list_filter = ('capacity',)
    search_fields = ('car_name',)


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'email', 'phone')
    search_fields = ('name', 'email')


@admin.register(TV)
class TvAdmin(admin.ModelAdmin):
    list_display = ('tv_model', 'price', 'specification', 'manufacturer')
    search_fields = ('tv_model', 'price')


@admin.register(Specifications)
class SpecificationsAdmin(admin.ModelAdmin):
    list_display = ('name', 'matrix', 'powerboard', 'mainplata', 'loudspeakers', 'casebox')
    search_fields = ('tv_model', 'price')


@admin.register(StaffStorage)
class StaffStorageAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position')
    search_fields = ('full_name', 'position')


@admin.register(StaffConstructor)
class StaffConstructorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position')
    search_fields = ('full_name', 'position')


@admin.register(Storehouse)
class StorehouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'capacity')
    search_fields = ('name',)


@admin.register(BuildLine)
class BuildLineAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Build)
class BuildAdmin(admin.ModelAdmin):
    list_display = ('build_date', 'tv', 'count', 'line', 'staff')
    list_filter = ('build_date', 'line')
    search_fields = ('name', 'tv')


@admin.register(Powerboard)
class PowerboardAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'power')
    search_fields = ('name', 'power')


@admin.register(Loudspeakers)
class LoudspeakersAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'count')
    search_fields = ('name', 'count')


@admin.register(Matrix)
class MatrixAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'contrast', 'resolution', 'matrix_type')
    list_filter = ('matrix_type',)
    search_fields = ('name', 'contrast')


@admin.register(MatrixType)
class MatrixTypeAdmin(admin.ModelAdmin):
    list_display = ('type_name',)
    search_fields = ('type_name',)


@admin.register(CaseBox)
class CaseBoxAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'width', 'length', 'depth')
    search_fields = ('name',)


@admin.register(Mainplata)
class MainplataAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)


admin.site.site_title = 'TV Company'
admin.site.site_header = 'Управление Телевизорами'
