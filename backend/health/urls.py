from django.urls import path
from .views import HealthCheckView, ReadinessCheckView

urlpatterns = [
    path('health/', HealthCheckView.as_view(), name='health-check'),
    path('ready/', ReadinessCheckView.as_view(), name='readiness-check'),
]
