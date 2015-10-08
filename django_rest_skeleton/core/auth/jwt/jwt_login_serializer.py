from django.contrib.auth import authenticate

from rest_framework import serializers

from .jwt import create_jwt_token


class JWTLoginSerializer(serializers.Serializer):
    """
    Serializer class used to validate a username and password.
    'username' is identified by the custom UserModel.USERNAME_FIELD.
    Returns a JSON Web Token that can be used to authenticate later calls.

    Adapted from:
    https://github.com/GetBlimp/django-rest-framework-jwt/blob/master/rest_framework_jwt/serializers.py
    """
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    MISSING_CREDENTIALS = 'Must include "email" and "password"'
    INVALID_CREDENTIALS = 'Unable to login with provided credentials.'
    USER_NOT_ACTIVE = 'User account is disabled.'

    def validate(self, data):
        """
        Validate an email and password
        Return an Account and the Account's JWT Token if successfully validated
        """
        # Create credentials
        credentials = {
            'email': data.get('email'),
            'password': data.get('password'),
        }

        # Assert that all of the user credentials are present
        if not all(credentials.values()):
            raise serializers.ValidationError(self.MISSING_CREDENTIALS)

        # Attempt to authenticate the user
        user = authenticate(**credentials)

        # If the returned object is None or the user is inactive do not issue token
        if user is None:
            raise serializers.ValidationError(self.INVALID_CREDENTIALS)
        if not user.is_active:
            raise serializers.ValidationError(self.USER_NOT_ACTIVE)

        # Create token and token expiration date
        token, expiration = create_jwt_token(user)

        # Return JSON Data
        return {
            'user': user,
            'token': token,
            'token_expiration': expiration
        }