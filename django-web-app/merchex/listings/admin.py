from django.contrib import admin
from listings.models import Band
from listings.models import Contact

class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'danger_level')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'band')

admin.site.register(Band, BandAdmin)
admin.site.register(Contact, ContactAdmin)