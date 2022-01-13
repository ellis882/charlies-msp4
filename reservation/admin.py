from django.contrib import admin
from .models import Table, Reservation


class TableAdmin(admin.ModelAdmin):
    list_display = ['table_nr', 'table_size']


admin.site.register(Table, TableAdmin)
admin.site.register(Reservation)
