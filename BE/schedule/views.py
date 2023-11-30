from rest_framework.viewsets import ModelViewSet
from .serializers import ScheduleSerializer
from .models import Schedule


class CustomScheduleViewSet(ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
