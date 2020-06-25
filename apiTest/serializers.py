# Api serializers
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validationData):
        user = User()
        user.first_name = validationData.get('first_name')
        user.last_name = validationData.get('last_name')
        user.username = validationData.get('username')
        user.email = validationData.get('email')
        user.set_password(validationData.get('password'))

        user.save()

    def validate_user(self, data):
        user = User.objects.filter(username=data)
        if(user):
            raise serializers.ValidationError("This username is alredy taken")
        else:
            return data
