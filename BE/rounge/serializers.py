from .models import Post
from django.contrib.auth import get_user_model
from allauth.account.adapter import get_adapter
from allauth.utils import email_address_exists
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer


class CustomPostCreateSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post

        fields = ['pk', 'author', 'title', 'created_at',
                  'updated_at', 'schedule', 'content']
