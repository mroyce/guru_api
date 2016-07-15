from rest_framework import status, viewsets, mixins
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response

from guru_api.core.models import User, InstructorProfile
from guru_api.core.serializers import UserSerializer, InstructorProfileSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    Endpoint for `User` Model
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = ()
    filter_fields = ()

    # @list_route(methods=['get'], url_path='instructor-profile', serializer_class=InstructorProfileSerializer)
    # def instructor_profile_get_list(self, request):
    #     """
    #     Get the InstructorProfile of the current user
    #     """
    #     user = self.request
    #     instructor_profile = user.instructor_profile

    #     # Check if the user has an instructor_profile to display
    #     if instructor_profile is not None:
    #         serializer = self.get_serializer(instructor_profile)
    #         return Response(serializer.data)
    #     else:
    #         return Response({}, status=status.HTTP_404_NOT_FOUND)

    # @detail_route(methods=['get'], url_path='instructor-profile', serializer_class=InstructorProfileSerializer)
    # def instructor_profile_get_detail(self, request, pk=None):
    #     """
    #     Get the InstructorProfile of the specified user
    #     """
    #     user = self.get_object()
    #     instructor_profile = user.instructor_profile

    #     # Check if the user has an instructor_profile to display
    #     if instructor_profile is not None:
    #         serializer = self.get_serializer(instructor_profile)
    #         return Response(serializer.data)
    #     else:
    #         return Response({}, status=status.HTTP_404_NOT_FOUND)

    # @list_route(methods=['post'], url_path='instructor-profile', serializer_class=InstructorProfileSerializer)
    # def instructor_profile_post(self, request):
    #     """
    #     Create (activate) an InstructorProfile for the current user
    #     """
    #     user = self.request
    #     instructor_profile = user.instructor_profile

    #     # Check if the user already has an instructor_profile
    #     if instructor_profile is None:
    #         instructor_profile = InstructorProfile.objects.create({'user': user})
    #         serializer = self.get_serializer(instructor_profile)
    #         serializer.is_valid(raise_exception=True)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         # Activate the user's instructor_profile
    #         if not instructor_profile.active:
    #             instructor_profile.active = True
    #             instructor_profile.save()
    #             serializer = self.get_serializer(instructor_profile)
    #             serializer.is_valid(raise_exception=True)
    #             return Response(serializer.data, status=status.HTTP_201_CREATED)
    #         # User has an active instructor_profile already
    #         else:
    #             return Response({}, status=status.HTTP_403_FORBIDDEN)

    # @list_route(methods=['put'], url_path='instructor-profile')
    # def instructor_profile_put(self, request):
    #     """
    #     Update the InstructorProfile of the current user
    #     """
    #     user = request.user
    #     instructor_profile = user.instructor_profile

    #     instructor_profile.update(request)
    #     instructor_profile.save()

    #     return Response({}, status=status.HTTP_200_OK)

    # @list_route(methods=['delete'], url_path='instructor-profile')
    # def instructor_profile_delete(self, request):
    #     """
    #     Delete (deactivate) the InstructorProfile of the current user
    #     """
    #     user = request.user
    #     instructor_profile = user.instructor_profile

    #     # Check if the user has an instructor_profile to delete
    #     if instructor_profile is not None:
    #         instructor_profile.active = False
    #         instructor_profile.save()
    #         return Response({}, status=status.HTTP_204_NO_CONTENT)
    #     # Use doesn't have an instructor_profile
    #     else:
    #         return Response({}, status=status.HTTP_403_FORBIDDEN)
