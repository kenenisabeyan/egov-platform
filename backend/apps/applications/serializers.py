from rest_framework import serializers

from .models import Application


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['id', 'applicant', 'service', 'full_name', 'phone', 'remarks', 'status', 'submitted_at', 'updated_at']
        read_only_fields = ['id', 'applicant', 'status', 'submitted_at', 'updated_at']
