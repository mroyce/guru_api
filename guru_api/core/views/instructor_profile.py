from rest_framework import viewsets, mixins

from guru_api.core.models import InstructorProfile
from guru_api.core.serializers import InstructorProfileSerializer
from guru_api.core.permissions import IsOwnerOrReadOnly


class InstructorProfileViewSet(viewsets.GenericViewSet,
                        	   mixins.RetrieveModelMixin,
                        	   mixins.CreateModelMixin,
                        	   mixins.UpdateModelMixin,
                        	   mixins.DestroyModelMixin):
    """
    Endpoint for Instructor Profiles
    """
    queryset = InstructorProfile.objects.filter(is_active=True)
    serializer_class = InstructorProfileSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    filter_fields = ()
