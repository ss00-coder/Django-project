from rest_framework import serializers

import Foreign_us
from notice.models import Notice, NoticeReply


class MainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foreign_us
        fields = '__all__'
