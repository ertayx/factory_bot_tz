from rest_framework import serializers
from .models import TelegramMessage

class TelegramMessageSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.pk')

    class Meta:
        model = TelegramMessage
        fields = '__all__'

    def create(self, validated_data):
        return super().create(validated_data)