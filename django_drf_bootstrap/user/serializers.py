from django.contrib.auth import get_user_model
from djoser import serializers as djoser_serializers

User = get_user_model()

class UserSerializer(djoser_serializers.UserSerializer):

    class Meta:
        model = User
        fields = ["id", "username", "email"]
