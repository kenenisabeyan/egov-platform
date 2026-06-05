from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from django.utils import timezone
from .models import Notification
from .serializers import NotificationSerializer


class NotificationViewSet(ModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)

    @action(detail=False, methods=['post'])
    def mark_all_as_read(self, request):
        Notification.objects.filter(user=request.user, read=False).update(
            read=True, read_at=timezone.now()
        )
        return Response({'status': 'All notifications marked as read'})

    @action(detail=True, methods=['post'])
    def mark_as_read(self, request, pk=None):
        notification = self.get_object()
        notification.read = True
        notification.read_at = timezone.now()
        notification.save()
        return Response({'status': 'Notification marked as read'})

    @action(detail=False, methods=['get'])
    def unread_count(self, request):
        count = Notification.objects.filter(user=request.user, read=False).count()
        return Response({'unread_count': count})
