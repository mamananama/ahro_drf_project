from .models import CustomUser
from django.contrib.auth import get_user_model
from allauth.account.adapter import get_adapter
from allauth.utils import email_address_exists
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer


class CustomRegisterSerializer(RegisterSerializer):
    password1 = serializers.CharField(max_length=128)
    password2 = serializers.CharField(max_length=128)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']
        extra_kwargs = {'password1': {'wrtie_only': True}}

    def validate_username(self, username):
        if get_user_model().objects.filter(username__iexact=username).exists():
            raise serializers.ValidationError("이미 사용중인 아이디입니다.")
        return username

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if email and email_address_exists(email):
            raise serializers.ValidationError("이미 사용중인 이메일입니다.")
        return email

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("비밀번호가 일치하지 않습니다.")
        return data

    def create(self, validated_data):
        password = validated_data.pop('password1', None)
        model = self.Meta.model(**validated_data)
        if password is not None:
            model.set_password(password)
        model.save()
        return model


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'email',
        ]
