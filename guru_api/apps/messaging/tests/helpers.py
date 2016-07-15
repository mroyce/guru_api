from guru_api.apps.messaging.models import Inbox, Message


def create_test_inbox(**kwargs):
    """
    Create and return a test image as a ContentFile
    """
    return Inbox.objects.create(**create_kwargs)


def create_test_message(inbox, posted_by, text='Test message', **kwargs):
    """
    Create and return a test Message object
    """
    create_kwargs = {
        'inbox': inbox,
        'posted_by': posted_by,
        'text': text,
    }

    create_kwargs.update(kwargs)
    return Message.objects.create(**create_kwargs)
