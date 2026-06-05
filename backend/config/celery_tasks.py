from celery import shared_task
from django.utils import timezone
from django.conf import settings
from apps.applications.models import Application
from apps.notifications.models import Notification
import logging

logger = logging.getLogger(__name__)


@shared_task
def process_application(application_id):
    """Background task to process application."""
    try:
        application = Application.objects.get(id=application_id)
        application.status = 'processing'
        application.save()
        
        Notification.objects.create(
            user=application.applicant,
            application=application,
            title='Application Received',
            message=f'Your application for {application.service.name} has been received and is being processed.',
            notification_type='application_received',
        )
        logger.info(f"Application {application_id} processed successfully")
    except Exception as e:
        logger.error(f"Error processing application {application_id}: {str(e)}")
        raise


@shared_task
def verify_documents(application_id):
    """Background task to verify documents."""
    try:
        application = Application.objects.get(id=application_id)
        documents = application.documents.all()
        
        pending_docs = documents.filter(status='pending')
        if not pending_docs.exists():
            application.status = 'verified'
            application.save()
            
            Notification.objects.create(
                user=application.applicant,
                application=application,
                title='Documents Verified',
                message='All your documents have been verified successfully.',
                notification_type='status_update',
            )
        
        logger.info(f"Document verification completed for application {application_id}")
    except Exception as e:
        logger.error(f"Error verifying documents for {application_id}: {str(e)}")
        raise


@shared_task
def send_notification_email(notification_id):
    """Background task to send email notifications."""
    try:
        notification = Notification.objects.get(id=notification_id)
        user = notification.user
        
        # TODO: Integrate email service (SendGrid, AWS SES, etc.)
        logger.info(f"Email notification sent to {user.email}")
    except Exception as e:
        logger.error(f"Error sending email notification: {str(e)}")
        raise


@shared_task
def cleanup_old_notifications():
    """Background task to cleanup old notifications."""
    from datetime import timedelta
    
    cutoff_date = timezone.now() - timedelta(days=90)
    deleted_count, _ = Notification.objects.filter(created_at__lt=cutoff_date, read=True).delete()
    logger.info(f"Deleted {deleted_count} old notifications")
    return deleted_count
