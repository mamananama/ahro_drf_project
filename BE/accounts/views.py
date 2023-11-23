from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthorOrReadOnly
from rest_framework.response import Response


class ProfileViewSet(ModelViewSet):
    lookup_field = 'username'
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated,
                          IsAuthorOrReadOnly]

    def get(self, request):
        content = {
            'test_message': f'반갑습니다, {str(request.user)} 님!',
        }
        print(f'profile {content}')
        return Response(content)
