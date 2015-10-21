from django.contrib import admin

from .models import Worker
# Register your models here.

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'account',)

#class OrderInline(admin.StackedInline):
#    model = Order
#    extra = 1



#@admin.register(Order)
#class OrderAdmin(admin.ModelAdmin):
#    list_display = ('event', 'item', 'user',)
