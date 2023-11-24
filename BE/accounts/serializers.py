from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers


class ProfileSerializer(ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'email',
        ]
