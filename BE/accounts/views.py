from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views.generic import DetailView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from dj_rest_auth.registration.views import RegisterView

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import ProfileSerializer, CustomRegisterSerializer
from .permissions import IsAuthorOrReadOnly


class ProfileViewSet(ModelViewSet):
    lookup_field = 'username'  # username으로 proifle 조회
    queryset = get_user_model().objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def get(self, request):
        content = {
            'test_message': f'반갑습니다, {str(request.user)} 님!',
        }
        return Response(content)


class UserCreate(RegisterView):
    serializer_class = CustomRegisterSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_info(request):
    print(request.data)
    content = {'message': 'Hello, World!', 'username': str(request.user)}
    return Response(content)
