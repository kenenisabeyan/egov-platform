from rest_framework import generics, permissions, status, filters
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django_filters.rest_framework import DjangoFilterBackend
from .models import Document
from .serializers import DocumentSerializer, DocumentUploadSerializer
from .utils import validate_document_file


class DocumentUploadView(generics.CreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentUploadSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        file = serializer.validated_data.get('file')
        validation = validate_document_file(file)
        if not validation['valid']:
            return Response({'errors': validation['errors']}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save(file_hash=validation['file_hash'], file_size=validation['file_size'])


class DocumentListView(generics.ListAPIView):
    serializer_class = DocumentSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'document_type', 'application']
    search_fields = ['document_type']
    ordering_fields = ['uploaded_at', 'verified_at']
    ordering = ['-uploaded_at']

    def get_queryset(self):
        application_id = self.request.query_params.get('application_id')
        if application_id:
            return Document.objects.filter(application_id=application_id)
        return Document.objects.filter(application__applicant=self.request.user)


class DocumentDetailView(generics.RetrieveUpdateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [permissions.IsAuthenticated]
