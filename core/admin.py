from django.contrib import admin
from .models import Cafe, Spot, Booking


@admin.register(Cafe)
class CafeAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'members_only', 'submitted_by', 'created_on')
    search_fields = ['name', 'city']
    list_filter = ('city', 'members_only')


admin.site.register(Spot)
admin.site.register(Booking)
