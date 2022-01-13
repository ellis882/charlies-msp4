from django.contrib import admin
from .models import Menu, Category, Specials


class MenuAdmin(admin.ModelAdmin):
    list_display = ['meal', 'category', 'price']
    search_fields = ['meal', 'category']
    list_filter = ['category']


admin.site.register(Menu, MenuAdmin)
admin.site.register(Category)
admin.site.register(Specials)
