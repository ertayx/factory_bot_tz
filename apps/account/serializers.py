from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.utils.text import gettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, max_length=20,
                                     required=True, write_only=True)
    password_confirmation = serializers.CharField(min_length=6, max_length=20,
                                                  required=True, write_only=True)

    class Meta:
        model = User
        fields = ('password', 'password_confirmation',
                  'first_name')

    def validate(self, attrs):
        password = attrs['password']
        password_confirmation = attrs.pop('password_confirmation')

        if password != password_confirmation:
            raise serializers.ValidationError(
                'Пароли должны быть похожи'
            )

        if password.isdigit() or password.isalpha():
            raise serializers.ValidationError(
                'Пароль должен содержать буквы и цифры'
                                )

        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user



class RefreshTokenSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_messages = {
        'bad_token': _('Token is invalid or expired')
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token')


class TokenSerializer(serializers.ModelSerializer):
    telegram_token = serializers.ReadOnlyField(source='token')

    class Meta:
        model = User
        fields = ['telegram_token']