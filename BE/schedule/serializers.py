from .models import Schedule
from django.contrib.auth import get_user_model
from allauth.account.adapter import get_adapter
from allauth.utils import email_address_exists
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer


class ScheduleSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='accounts.CustomUser.username')

    class Meta:
        model = Schedule
        fields = ['owner', 'title', 'start_at', 'end_at', 'content']
