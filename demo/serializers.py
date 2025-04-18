from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from demo.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data.get("email"),
            password=validated_data.get("password")
        )
        return user

class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'email'

    def validate(self, attrs):
        data = super().validate(attrs)
        # 重命名 refresh 为 refresh_token
        data["refresh_token"] = data.pop("refresh")
        data['access_token'] = data.pop("access")
        return data
