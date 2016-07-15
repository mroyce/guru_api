from django.conf import settings
from django.db import models

from guru_api.core.base.model import BaseGuruModel


class Inbox(BaseGuruModel):
    """
    Inbox Model
    """
    accounts = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='inboxes')
