from rest_framework import serializers
from notice.models import Notice, NoticeReply


class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = '__all__'


class NoticeReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = NoticeReply
        fields = '__all__'