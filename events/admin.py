from django.contrib import admin
from .models import Events, EventImage


class EventsAdmin(admin.ModelAdmin):  # instead of ModelAdmin
    list_display = ['name', 'phone', 'type_of_event', 'Date_of_event']
    search_fields = ['name', 'Date_of_event', 'type_of_event']
    list_filter = ('name', 'number_of_persons')


admin.site.register(Events, EventsAdmin)
admin.site.register(EventImage)
