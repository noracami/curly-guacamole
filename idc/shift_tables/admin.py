from django.contrib import admin

from .models import Shift, Table
# Register your models here.

@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ('date',)

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('date',)

#class OrderInline(admin.StackedInline):
#    model = Order
#    extra = 1



#@admin.register(Order)
#class OrderAdmin(admin.ModelAdmin):
#    list_display = ('event', 'item', 'user',)
