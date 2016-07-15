from django.db import models

from guru_api.core.base.model import BaseGuruModel


class PaymentMethod(BaseGuruModel):
    """
    PaymentMethod Model
    """
    account = models.ForeignKey('core.Account', related_name='payment_methods')

    stripe_id = models.CharField(max_length=100, unique=True)
