import os

from django.db import models
from django.core.validators import RegexValidator
from django.utils.crypto import get_random_string

from guru_api.core.upload_paths import user_upload_path
from guru_api.core.models.account import Account, AccountManager


class UserManager(AccountManager):
    """
    User Manager
    """
    def create(self, *args, **kwargs):
        """
        Create a new User and associated Account
        """
        # Create the Account for this User
        self.create_user(*args, **kwargs)

        # Create the User
        user = self.model(*args,**kwargs)
        user.save()
        return user
        

class User(Account):
    """
    User Model
    """
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    avatar = models.ImageField(max_length=256, blank=True, null=True, upload_to=user_upload_path)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'.")
    phone_number = models.CharField(validators=[phone_regex], blank=True, null=True, max_length=15)

    objects = UserManager()
