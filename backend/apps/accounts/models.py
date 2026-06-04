from django.contrib.auth.models import AbstractUser
from django.db import models
from apps.tenants.models import Tenant

class User(AbstractUser):
    ROLE_CHOICES = (
        ('citizen', 'Citizen'),
        ('officer', 'Government Officer'),
        ('dept_head', 'Department Head'),
        ('admin', 'Tenant Admin'),
        ('superadmin', 'Platform Super Admin'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='citizen')
    phone = models.CharField(max_length=15, unique=True)
    email_verified = models.BooleanField(default=False)
    phone_verified = models.BooleanField(default=False)
    mfa_enabled = models.BooleanField(default=False)
    mfa_secret = models.CharField(max_length=32, blank=True)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='users', null=True)

    def __str__(self):
        return f"{self.username} ({self.role})"