from rest_framework import serializers

from guru_api.apps.messaging.models import Inbox


class InboxSerializer(serializers.ModelSerializer):
    """
    Inbox Model Serializer
    """
    class Meta:
        model = Inbox

        fields = (
            'id',
            'accounts',
        )
