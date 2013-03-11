from django.conf import settings
from django.db.models import signals

if "notification" in settings.INSTALLED_APPS:
    from notification.models import NoticeType

    def create_notice_types(app, created_models, verbosity, **kwargs):
        NoticeType.create("received_email", "Private messages", "(this is highly recommended)")
    import notification
    signals.post_syncdb.connect(create_notice_types, sender=notification.models)
else:
    print "Skipping creation of NoticeTypes (Threaded Messages) as notification app not found"
