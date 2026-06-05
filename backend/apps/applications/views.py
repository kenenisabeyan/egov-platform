from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Application
from .serializers import ApplicationSerializer


class ApplicationCreateView(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(applicant=self.request.user)


class ApplicationListView(generics.ListAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'service']
    search_fields = ['full_name', 'phone', 'service__name']
    ordering_fields = ['submitted_at', 'updated_at']
    ordering = ['-submitted_at']

    def get_queryset(self):
        return Application.objects.filter(applicant=self.request.user)


class ApplicationDetailView(generics.RetrieveAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]
