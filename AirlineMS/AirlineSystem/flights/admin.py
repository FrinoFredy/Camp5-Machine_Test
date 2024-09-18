from django.contrib import admin
from .models import Flight


class FlightAdmin(admin.ModelAdmin):
    list_display = ('flight_id', 'dep_airport', 'dep_date', 'arr_airport', 'arr_date')
    search_fields = ('flight_id', 'dep_airport', 'arr_airport')
    list_filter = ('dep_date', 'arr_date')
    ordering = ('dep_date',)


admin.site.register(Flight, FlightAdmin)

