# admin.py
from django.contrib import admin
from .models import Duureg, Address
class AddressAdmin(admin.ModelAdmin):
    list_display = ('street_address', 'city', 'state', 'postal_code')
    search_fields = ('street_address', 'city', 'state', 'postal_code')
    list_filter = ('state', 'city')

admin.site.register(Address, AddressAdmin)

class DuuregAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Duureg, DuuregAdmin)
