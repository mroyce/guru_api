from rest_framework import serializers

from guru_api.apps.parment.models import PaymentMethod


class PaymentMethodSerializer(serializers.ModelSerializer):
    """
    PaymentMethod Model Serializer
    """
    class Meta:
        model = PaymentMethod

        fields = (
            'id',
            'stripe_id',
            'account',
        )

        extra_kwargs = {
            'stripe_id': {'write_only': True},
        }