from rest_framework import status, viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response

from ..models import User
from ..serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    Endpoint for `User` Model
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_fields = ()

    @list_route(methods=['post'], url_path='set-password')
    def set_password(self, request):
        """
        `/users/set-password/`
        Set the password for the currently logged in  `User`
        """
        user = request.user
        if user.is_authenticated:
            user.set_password(request.password)
            return Response({}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({}, status=status.HTTP_403_FORBIDDEN)
