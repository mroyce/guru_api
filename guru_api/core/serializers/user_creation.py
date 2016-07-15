from rest_framework import serializers

from guru_api.core.models import User
from guru_api.core.models.account import Account


class UserCreationSerializer(serializers.ModelSerializer):
    """
    User Model Serializer
    """
    class Meta:
        model = User

        fields = (
            'id',
            'email',
            'password',
            'first_name',
            'last_name',
        )

        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        """
        Create and return a new User, given the validated data.
        Create a new Account object for the User.
        """
        Account.objects.create_user(**validated_data)
        return User.objects.create(**validated_data)
