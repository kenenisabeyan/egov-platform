from django.urls import path
from .views import ApplicationCreateView, ApplicationListView, ApplicationDetailView

urlpatterns = [
    path('', ApplicationListView.as_view(), name='application-list'),
    path('create/', ApplicationCreateView.as_view(), name='application-create'),
    path('<int:pk>/', ApplicationDetailView.as_view(), name='application-detail'),
]
