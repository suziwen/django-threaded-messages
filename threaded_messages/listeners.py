from django.utils.html import strip_tags
from django.conf import settings
from utils import reply_to_thread
from utils import strip_quotes
import logging
logger = logging.getLogger('gidsy.apps.sendgrid')

if sendgrid_settings.THREADED_MESSAGES_USE_SENDGRID:
    from sendgrid_parse_api.utils import email_received

def signal_received_email(sender, sma, app_id, html, text, from_field, **kwargs):
    logger.debug("Sendgrid signal receive: %s, %s, %s, %s, %s, %s"%(sender, sma, app_id,
                                                                    html, text, from_field) )
    if app_id == settings.THREADED_MESSAGES_ID:
        body =''

        if text:
            body = text

        if not body:
            body = strip_tags(html)
               
        if body:
            strip_quotes(body)
            thread = sma.content_object
            reply_to_thread(thread, sma.user, body)

def start_listening():
    logger.debug("Sendgrid start listening")
    email_received.connect(signal_received_email, dispatch_uid="thm_reply")
