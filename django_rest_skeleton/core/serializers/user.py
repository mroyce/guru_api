from rest_framework import serializers

from ..models import User


class UserSerializer(serializers.ModelSerializer):
    """
    User Model Serializer
    """
    class Meta:
        model = User

        fields = (
            'id',
            'created_at',
            'last_updated',
            'email',
            'password',
            'first_name',
            'last_name',
            'gender',
            'profile_picture',
        )
        
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        """
        Create and return a new User, given the validated data.
        Also create a Token and AuthToken object for the new User.
        """
        # Create new User
        return User.objects.create_user(**validated_data)
