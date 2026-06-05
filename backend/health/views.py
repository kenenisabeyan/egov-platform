from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.db import connection
from django.conf import settings
from django.core.cache import cache
import logging

logger = logging.getLogger(__name__)


class HealthCheckView(APIView):
    """Health check endpoint for monitoring."""
    
    def get(self, request):
        try:
            # Check database
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
            db_status = 'ok'
        except Exception as e:
            db_status = f'error: {str(e)}'
            logger.error(f"Database health check failed: {e}")

        try:
            # Check cache
            cache.set('health_check', 'ok', 10)
            cache_status = 'ok'
        except Exception as e:
            cache_status = f'error: {str(e)}'
            logger.error(f"Cache health check failed: {e}")

        is_healthy = db_status == 'ok' and cache_status == 'ok'
        
        return Response({
            'status': 'healthy' if is_healthy else 'unhealthy',
            'database': db_status,
            'cache': cache_status,
            'debug': settings.DEBUG,
        }, status=status.HTTP_200_OK if is_healthy else status.HTTP_503_SERVICE_UNAVAILABLE)


class ReadinessCheckView(APIView):
    """Readiness check endpoint - whether service is ready to accept traffic."""
    
    def get(self, request):
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
            return Response({'ready': True}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Readiness check failed: {e}")
            return Response({'ready': False, 'error': str(e)}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
