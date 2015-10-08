import os

from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.crypto import get_random_string


def _generate_jwt_secret_key():
    """
    Create a user-specific jwt_secret_key.
    """
    jwt_secret_key_length = User._meta.get_field('jwt_secret_key').max_length
    return get_random_string(jwt_secret_key_length, settings.SECRET_KEY_CHARACTER_SET)


class UserManager(BaseUserManager):
    """
    User Manager
    Extends django.contrib.auth.models.BaseUserManager
    https://docs.djangoproject.com/en/1.8/topics/auth/customizing/#django.contrib.auth.models.BaseUserManager
    """
    def create_user(self, email, password=None, *args, **kwargs):
        """
        Create a new User
        Also assign the user an auth_token
        https://docs.djangoproject.com/en/dev/topics/auth/customizing/#django.contrib.auth.models.CustomUserManager.create_user
        """
        # Create User
        user = self.model(
            email=self.normalize_email(email),
            *args,
            **kwargs
        )

        # Save to database
        user.save()

        # Set password
        user.set_password(password)

        # Save changes to database
        user.save()
        return user

    def create_superuser(self, email, password, *args, **kwargs):
        """
        Creates a new User with `superuser` privileges
        https://docs.djangoproject.com/en/dev/topics/auth/customizing/#django.contrib.auth.models.CustomUserManager.create_superuser
        """
        # Create User
        user = self.create_user(
            email,
            password=password,
            *args,
            **kwargs
        )
        
        # Give User admin privileges and save changes
        user.is_admin = True
        user.save()
        return user


class User(AbstractBaseUser):
    """
    User Model
    Extends django.contrib.auth.models.AbstractBaseUser
    https://docs.djangoproject.com/en/1.8/topics/auth/customizing/#django.contrib.auth.models.AbstractBaseUser
    """
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    jwt_secret_key = models.CharField(default=_generate_jwt_secret_key, max_length=30, editable=False)

    objects = UserManager()

    # This is required to make email field the default identifier
    # https://docs.djangoproject.com/en/dev/topics/auth/customizing/#django.contrib.auth.models.CustomUser.USERNAME_FIELD
    USERNAME_FIELD = 'email'

    # This is required for when creating a user via the createsuperuser management command
    # https://docs.djangoproject.com/en/dev/topics/auth/customizing/#django.contrib.auth.models.CustomUser.REQUIRED_FIELDS
    REQUIRED_FIELDS = ['first_name', 'last_name',]

    def is_active(self):
        """
        Return whether the user is considered active
        https://docs.djangoproject.com/en/dev/topics/auth/customizing/#django.contrib.auth.models.CustomUser.is_active
        """
        return True

    def get_full_name(self):
        """
        Return unique identifier for the user
        https://docs.djangoproject.com/en/dev/topics/auth/customizing/#django.contrib.auth.models.CustomUser.get_full_name
        """
        return self.email

    def get_short_name(self):
        """
        Return informal identifier for the user
        https://docs.djangoproject.com/en/dev/topics/auth/customizing/#django.contrib.auth.models.CustomUser.get_short_name
        """
        return self.first_name + ' ' + self.last_name

    def get_jwt_secret_key(self):
        """
        Sign JWTs with a combination of settings.JWT_MASTER_SECRET_KEY
        and self.jwt_secret_key
        """
        return '{}{}'.format(settings.JWT_MASTER_SECRET_KEY, self.jwt_secret_key)
