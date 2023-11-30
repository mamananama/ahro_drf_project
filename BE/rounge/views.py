from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import CustomPostCreateSerializer
from .models import Post
from .permissions import OnlyAuthorUpdateDelete, IsAuthorOrReadOnly


class CustomPostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = CustomPostCreateSerializer
    permission_classes = [OnlyAuthorUpdateDelete]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def list(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-pk')
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)
