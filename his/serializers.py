from rest_framework import serializers
from his.models import Hi

class HiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hi
        fields = (
            'hi',
            'timestamp',
            'sender',
        )

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hi
        fields = (
            'message',
            'timestamp',
            'sender',
        )
