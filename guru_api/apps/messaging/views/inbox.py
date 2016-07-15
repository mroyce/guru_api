from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from guru_api.apps.messaging.models import Inbox, Message
from guru_api.apps.messaging.serializers import InboxSerializer, MessageSerializer


class InboxViewSet(viewsets.ModelViewSet):
    """
    Endpoint for `Inbox` Model
    """
    queryset = Inbox.objects.all()
    serializer_class = InboxSerializer
    filter_fields = ()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
    	user = self.request.user
    	return user.inboxes.all()

    # @detail_route(methods=['get'], url_path='messages', serializer_class=MessageSerializer)
    # def messages_get(self, request, pk=None):
    # 	"""
    # 	Get all messages from this inbox
    # 	"""
    # 	inbox = self.get_object()
    # 	messages = inbox.messages.all()

    # 	serializer = self.get_serializer(messages)
    # 	return Response(serializer.data)
