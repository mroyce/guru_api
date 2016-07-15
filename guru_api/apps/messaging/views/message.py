from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from guru_api.apps.messaging.models import Message
from guru_api.apps.messaging.serializers import MessageSerializer


class MessageViewSet(viewsets.ModelViewSet):
    """
    Endpoint for `Message` Model
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_fields = ()
    permission_classes = (IsAuthenticated,)
