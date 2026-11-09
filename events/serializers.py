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
        
    def validate(self, data):
        event = data['event']
        user = self.context['request'].user

        if Registration.objects.filter(event=event, attendee=user).exists():
            raise serializers.ValidationError("You're already registered for this event.")
        if event.registrations.count() >= event.capacity:
            raise serializers.ValidationError("This event is full.")
        return data
