from django.contrib.auth.models import AbstractUser
from django.db import models
from django_tenants.models import TenantMixin, DomainMixin

class Tenant(TenantMixin):
    name = models.CharField(max_length=100)
    paid_until = models.DateField()
    on_trial = models.BooleanField(default=True)
    schema_name = models.CharField(max_length=63, unique=True)
    # custom fields
    country = models.CharField(max_length=2)  # ET, KE, NG, etc.
    language_default = models.CharField(max_length=5, default='en')
    created_at = models.DateTimeField(auto_now_add=True)
    auto_create_schema = True

class Domain(DomainMixin):
    pass

class User(AbstractUser):
    ROLE_CHOICES = (
        ('citizen', 'Citizen'),
        ('officer', 'Government Officer'),
        ('dept_head', 'Department Head'),
        ('admin', 'System Admin'),
        ('superadmin', 'Platform Super Admin'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='citizen')
    phone = models.CharField(max_length=15, unique=True)
    email_verified = models.BooleanField(default=False)
    phone_verified = models.BooleanField(default=False)
    mfa_enabled = models.BooleanField(default=False)
    mfa_secret = models.CharField(max_length=32, blank=True)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='users')