from django.conf import settings
from django.db import models

from guru_api.core.base.model import BaseGuruModel


class Message(BaseGuruModel):
    """
    Message Model
    """
    inbox = models.ForeignKey('messaging.Inbox', related_name='messages')
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='messages')

    text = models.TextField()
