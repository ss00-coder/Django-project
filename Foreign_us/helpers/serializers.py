from rest_framework import serializers
from helpers.models import Helpers, HelpersReply


class HelpersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Helpers
        fields = '__all__'


class HelpersReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpersReply
        fields = '__all__'
