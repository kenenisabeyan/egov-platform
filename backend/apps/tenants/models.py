from django.db import models
from django_tenants.models import TenantMixin, DomainMixin

class Tenant(TenantMixin):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=2, default='ET')
    language_default = models.CharField(max_length=5, default='en')
    paid_until = models.DateField(null=True, blank=True)
    on_trial = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    auto_create_schema = True
    auto_drop_schema = True

class Domain(DomainMixin):
    pass
