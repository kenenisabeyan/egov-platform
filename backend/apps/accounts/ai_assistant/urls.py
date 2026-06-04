from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.chat, name='ai-chat'),
    path('check-document/', views.check_uploaded_document, name='check-doc'),
]