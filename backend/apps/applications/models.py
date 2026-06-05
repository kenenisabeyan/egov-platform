from django.db import models
from django.conf import settings
from apps.services.models import Service


class Application(models.Model):
    applicant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='applications')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='applications')
    full_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    remarks = models.TextField(blank=True)
    status = models.CharField(max_length=50, default='pending')
    submitted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-submitted_at']

    def __str__(self):
        return f"Application {self.id} for {self.service.name} by {self.full_name}"
