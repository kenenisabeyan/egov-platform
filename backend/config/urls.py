from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from apps.accounts.views import CustomTokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/accounts/', include('apps.accounts.urls')),
    path('api/tenants/', include('apps.tenants.urls')),
    path('api/citizens/', include('apps.citizens.urls')),
    path('api/services/', include('apps.services.urls')),
    path('api/applications/', include('apps.applications.urls')),
    path('api/documents/', include('apps.documents.urls')),
    path('api/ai/', include('apps.ai_assistant.urls')),
]