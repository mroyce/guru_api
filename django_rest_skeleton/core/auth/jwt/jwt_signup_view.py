from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .jwt import create_jwt_token, get_login_signup_response
from ...serializers import UserSerializer


class JWTSignUpView(APIView):
    """
    Endpoint to allow a new user to register for a new account.

    Returns a dictionary detailing the created user including a 'token' key
    with a JWT access token and JWT token expiration date.
    """
    # don't need to be authenticated or have permissions to create a new user
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer

    def post(self, request, format=None):
        """
        The endpoint processes `POST` requests with the required data: `email` and `password`.

        Given valid data, creates a new User and returns 201 with serialized session data
        and a JWT access token.

        If not valid, returns 400.
        """
        # Assert we have a valid new User object with new_user_serializer.is_valid()
        new_user_serializer = self.serializer_class(data=request.data)
        new_user_serializer.is_valid(raise_exception=True)

        # Save the new User
        new_user = new_user_serializer.save()

        # Create a token for the new User
        token, token_expiration = create_jwt_token(new_user)

        # Construct Response
        response_data = get_login_signup_response(new_user, token, token_expiration, request=request)
        return Response(response_data, status=status.HTTP_201_CREATED)
