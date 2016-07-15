from rest_framework import viewsets, mixins

from guru_api.core.models import User
from guru_api.core.serializers import UserProfileSerializer
from guru_api.core.permissions import IsOwnerOrReadOnly


class UserProfileViewSet(viewsets.GenericViewSet,
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin):
    """
    Endpoint for User Profiles
    """
    queryset = User.objects.filter(is_active=Truefa)
    serializer_class = UserProfileSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    filter_fields = ()
