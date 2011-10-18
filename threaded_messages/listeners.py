from django.conf import settings
from utils import reply_to_thread

def handle_received_email(sma, app_id, html, text, from_field):
	if app_id == settings.THREADED_MESSAGES_ID:
		reply_to_thread(sma.content_object, sma.user, html)
	
if "sendgrid_parse_api" in settings.INSTALLED_APPS:
	from sendgrid_parse_api.signals import email_received
	email_received.connect(handle_received_email)