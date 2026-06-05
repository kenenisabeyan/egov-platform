from django.db import models
from django.conf import settings
from apps.applications.models import Application


class Notification(models.Model):
    NOTIFICATION_TYPES = (
        ('application_received', 'Application Received'),
        ('application_approved', 'Application Approved'),
        ('application_rejected', 'Application Rejected'),
        ('document_request', 'Document Request'),
        ('status_update', 'Status Update'),
        ('general', 'General Notification'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='notifications', null=True, blank=True)
    title = models.CharField(max_length=200)
    message = models.TextField()
    notification_type = models.CharField(max_length=50, choices=NOTIFICATION_TYPES)
    read = models.BooleanField(default=False)
    read_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    data = models.JSONField(default=dict, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} for {self.user.username}"
