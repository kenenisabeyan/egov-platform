from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Service
from .serializers import ServiceSerializer


class ServiceListView(generics.ListAPIView):
    queryset = Service.objects.filter(is_active=True)
    serializer_class = ServiceSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['department']
    search_fields = ['name', 'description']
    ordering_fields = ['created_at', 'name']
    ordering = ['name']


class ServiceDetailView(generics.RetrieveAPIView):
    queryset = Service.objects.filter(is_active=True)
    serializer_class = ServiceSerializer
    permission_classes = [permissions.AllowAny]
