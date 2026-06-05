from django.db import models
from django.conf import settings
from apps.applications.models import Application


class Document(models.Model):
    DOCUMENT_TYPES = (
        ('id', 'ID Document'),
        ('proof_address', 'Proof of Address'),
        ('support', 'Supporting Document'),
        ('certificate', 'Certificate'),
        ('other', 'Other'),
    )
    STATUS_CHOICES = (
        ('pending', 'Pending Review'),
        ('verified', 'Verified'),
        ('rejected', 'Rejected'),
    )

    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='documents')
    document_type = models.CharField(max_length=20, choices=DOCUMENT_TYPES)
    file = models.FileField(upload_to='documents/%Y/%m/%d/')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    verification_notes = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    verified_at = models.DateTimeField(null=True, blank=True)
    file_size = models.BigIntegerField(default=0)
    file_hash = models.CharField(max_length=64, blank=True)

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return f"{self.document_type} for Application {self.application.id}"
