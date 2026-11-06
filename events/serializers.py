from rest_framework import serializers
from .models import Event, Registration, Session, Speaker


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ['id', 'title', 'start_time', 'end_time']


class EventSerializer(serializers.ModelSerializer):
    sessions = SessionSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'location', 'capacity', 'sessions']


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ['id', 'event', 'attendee', 'checked_in', 'registered_at']
        read_only_fields = ['attendee', 'checked_in', 'registered_at']