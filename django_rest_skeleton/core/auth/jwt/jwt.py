import jwt
from datetime import datetime

from django.conf import settings
from django.utils.encoding import smart_text

from rest_framework.authentication import BaseAuthentication, get_authorization_header

from ...models import User
from ...serializers import UserSerializer


LOGIN_SIGNUP_RESPONSE_USER_KEY = 'user'
LOGIN_SIGNUP_RESPONSE_JWT_KEY = 'jwt'
LOGIN_SIGNUP_RESPONSE_JWT_EXPIRATION_KEY = 'expiration'
JWT_USER_ID_PAYLOAD_KEY = 'sub'
JWT_EXPIRATION_PAYLOAD_KEY = 'exp'


def get_login_signup_response(user, token, token_expiration, request=None):
    """
    Return Response for login/signup endpoints
    Include data for User, JWT Token, and JWT Token Expiration
    ```
    {
      "user": {
        "id": "307",
        "first_name": "John G",
        ...
      },
      "jwt": "<token>",
      "expiration": "<expiration>"
    }
    ```
    """
    # Serialize User
    user_serialized = UserSerializer(user, context={'request': request})

    # Get datetime as Year-Month-Day Hour:Minute:Second format
    datetime.fromtimestamp(token_expiration).strftime("%Y-%m-%d %H:%M:%S")
    token_expiration_date_time_field = token_expiration

    # Construct response
    final_response = {}
    final_response[LOGIN_SIGNUP_RESPONSE_USER_KEY] = user_serialized.data
    final_response[LOGIN_SIGNUP_RESPONSE_JWT_KEY] = token
    final_response[LOGIN_SIGNUP_RESPONSE_JWT_EXPIRATION_KEY] = token_expiration_date_time_field

    return final_response


def create_jwt_token(user):
    """
    Create JWT token for the given `User`
    Create token and the token expiration date
    """
    # Get payload
    payload = create_user_jwt_payload(user)

    # Create token
    token = encode_jwt(payload, user)

    # Get expiration
    expiration = payload[JWT_EXPIRATION_PAYLOAD_KEY]

    return token, expiration


def create_user_jwt_payload(user):
    """
    Create JWT Payload
    The payload will contain:
    {
        'sub': user.pk,
        'exp': datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA
    }
    """
    payload = {}
    payload[JWT_USER_ID_PAYLOAD_KEY] = user.pk
    payload[JWT_EXPIRATION_PAYLOAD_KEY] = datetime.utcnow() + settings.JWT_EXPIRATION_DELTA
    return payload


def get_auth_header(request):
    """
    Returns the authentication header string split into
    [auth_header_prefix, token] or `None` if there is no authentication header.
    """
    token = get_authorization_header(request).split()
    auth_header_prefix = settings.JWT_AUTH_HEADER_PREFIX.lower()

    # If no Token was given or if prefix is not 'JWT', return None
    if not token or smart_text(token[0].lower()) != auth_header_prefix:
        return None

    # Check if length of Authroization Header is valid
    if len(token) == 1 or len(token) > 2:
        return None

    return token


def get_user_from_payload(payload):
    """
    Get the `User` from the payload
    """
    # Get user id from the payload
    user_id = payload.get(JWT_USER_ID_PAYLOAD_KEY, None)

    # Get user object with id=user_id
    user = User.objects.get(pk=user_id)

    return user


def encode_jwt(payload, user, algorithm=settings.JWT_ALGORITHM):
    """
    Encode the given payload dictionary as a JWT token
    """
    return jwt.encode(
        payload,
        user.get_jwt_secret_key(),
        algorithm
    ).decode('utf-8')


def decode_jwt(token, user, algorithms=[settings.JWT_ALGORITHM]):
    """
    Decode the given JWT token
    """
    return jwt.decode(
        token,
        user.get_jwt_secret_key(),
        algorithms=algorithms,
        leeway=settings.JWT_LEEWAY,
        options={'verify_exp': settings.JWT_VERIFY_EXPIRATION},
    )


class JWTAuthentication(BaseAuthentication):
    """
    Token based authentication using the JSON Web Token standard.
    Handle encoding/decoding of JWT
    Use Django Rest Framework JWT: https://github.com/GetBlimp/django-rest-framework-jwt
    """
    def authenticate(self, request):
        """
        Returns a two-tuple of `User` and token if a valid signature has been
        supplied using JWT-based authentication.  Otherwise returns `None`.
        """
        auth = get_auth_header(request)

        # Check if we successfully got a JWT
        if auth is None:
            return None

        token = auth[1]

        # Grab payload, but can't check signature yet because we need the `User`
        payload = jwt.decode(token, options={'verify_signature': False})

        # Get the associated `User`
        user = get_user_from_payload(payload)

        # Verify the signature
        payload = decode_jwt(token, user)

        return (user, token)
