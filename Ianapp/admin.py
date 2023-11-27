# admin.py
# admin.py
from django.contrib import admin
from .models import UserProfile, Location, Place

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar', 'bio')
    readonly_fields = ('user',)
    fieldsets = (
        (None, {'fields': ('user', 'avatar', 'bio')}),
    )

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('user', 'latitude', 'longitude')

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude')

