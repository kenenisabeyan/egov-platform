from rest_framework import serializers
from .models import Document


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'application', 'document_type', 'file', 'status', 'verification_notes', 'uploaded_at', 'verified_at', 'file_size', 'file_hash']
        read_only_fields = ['id', 'uploaded_at', 'verified_at', 'file_size', 'file_hash']


class DocumentUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'application', 'document_type', 'file', 'status']
        read_only_fields = ['id', 'status']
