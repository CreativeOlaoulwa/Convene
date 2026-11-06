from django.contrib import admin
from .models import Event, Session, Registration, Speaker

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'location', 'capacity', 'created_at']
    search_fields = ['title', 'location']

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ['title', 'event', 'start_time', 'end_time']
    list_filter = ['event']

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['attendee', 'event', 'registered_at', 'checked_in']
    list_filter = ['event', 'checked_in']
    list_editable = ['checked_in']

@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    list_display = ['name', 'session']