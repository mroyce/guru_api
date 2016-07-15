import os

from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.crypto import get_random_string

from guru_api.core.base.model import BaseGuruModel


def _generate_jwt_secret_key():
    """
    Create a user-specific jwt_secret_key.
    """
    jwt_secret_key_length = Account._meta.get_field('jwt_secret_key').max_length
    return get_random_string(jwt_secret_key_length, settings.SECRET_KEY_CHARACTER_SET)


class AccountManager(BaseUserManager):
    """
    Account Manager
    Extends django.contrib.auth.models.BaseUserManager
    """
    def create_user(self, email, password=None, *args, **kwargs):
        """
        Create a new Account
        Also assign the user an auth_token
        https://docs.djangoproject.com/en/dev/topics/auth/customizing/#django.contrib.auth.models.CustomUserManager.create_user
        """
        # Create Account
        account = self.model(
            email=self.normalize_email(email),
            *args,
            **kwargs
        )

        # Save to database
        account.save()

        # Set password
        account.set_password(password)

        # Save changes to database
        account.save()
        return account

    def create_superuser(self, email, password, *args, **kwargs):
        """
        Creates a new Account with `superuser` privileges
        https://docs.djangoproject.com/en/dev/topics/auth/customizing/#django.contrib.auth.models.CustomUserManager.create_superuser
        """
        # Create Account
        account = self.create_user(
            email,
            password=password,
            *args,
            **kwargs
        )
        
        # Give Account admin privileges and save changes
        account.is_admin = True
        account.save()
        return account


class Account(AbstractBaseUser, BaseGuruModel):
    """
    Account Model
    Extends django.contrib.auth.models.AbstractBaseUser
    """
    USER = 1
    ORGANIZATION = 2
    ACCOUNT_TYPE_CHOICES = (
        (USER, 'User'),
        (ORGANIZATION, 'Organization'),
    )

    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    account_type = models.PositiveSmallIntegerField(choices=ACCOUNT_TYPE_CHOICES, default=USER)
    jwt_secret_key = models.CharField(default=_generate_jwt_secret_key, max_length=30, editable=False)

    objects = AccountManager()

    # This is required to make email field the default identifier
    # https://docs.djangoproject.com/en/dev/topics/auth/customizing/#django.contrib.auth.models.CustomUser.USERNAME_FIELD
    USERNAME_FIELD = 'email'

    # This is required for when creating a user via the createsuperuser management command
    # https://docs.djangoproject.com/en/dev/topics/auth/customizing/#django.contrib.auth.models.CustomUser.REQUIRED_FIELDS
    REQUIRED_FIELDS = []

    def get_full_name(self):
        """
        Return unique identifier for the user
        https://docs.djangoproject.com/en/dev/topics/auth/customizing/#django.contrib.auth.models.CustomUser.get_full_name
        """
        return self.email

    def get_short_name(self):
        """
        Return informal identifier for the user
        https://docs.djangoproject.com/en/dev/topics/auth/customizing/#djangexio.contrib.auth.models.CustomUser.get_short_name
        """
        return self.email

    def get_jwt_secret_key(self):
        """
        Sign JWTs with a combination of settings.JWT_MASTER_SECRET_KEY
        and self.jwt_secret_key
        """
        return '{}{}'.format(settings.JWT_MASTER_SECRET_KEY, self.jwt_secret_key)

    def delete(self):
        """
        Don't delete the Account
        Instead just set `is_active` to False
        """
        self.is_active = False
        self.save()
        return self
