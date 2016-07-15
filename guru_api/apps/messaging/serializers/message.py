from rest_framework import serializers

from guru_api.apps.messaging.models import Message


class MessageSerializer(serializers.ModelSerializer):
    """
    Message Model Serializer
    """
    class Meta:
        model = Message

        fields = (
        	'id',
            'posted_by',
            'created_at',
            'text',
        )
