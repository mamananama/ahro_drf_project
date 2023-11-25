from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model
from .serializers import ProfileSerializer, CustomRegisterSerializer
from rest_framework.response import Response
from dj_rest_auth.registration.views import RegisterView


class ProfileViewSet(ModelViewSet):
    lookup_field = 'username'  # username으로 proifle 조회
    queryset = get_user_model().objects.all()
    serializer_class = ProfileSerializer
    permission_classes = ''  # [IsAuthenticated, IsAuthorOrReadOnly]

    def get(self, request):
        content = {
            'test_message': f'반갑습니다, {str(request.user)} 님!',
        }
        return Response(content)


class UserCreate(RegisterView):
    serializer_class = CustomRegisterSerializer
