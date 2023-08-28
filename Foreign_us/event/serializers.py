from rest_framework import serializers
from event.models import Event, EventReply


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class EventReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = EventReply
        fields = '__all__'
