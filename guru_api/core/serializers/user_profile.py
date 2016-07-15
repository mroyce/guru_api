from django.core.exceptions import ObjectDoesNotExist

from rest_framework import serializers

from guru_api.core.models import User


class UserProfileSerializer(serializers.ModelSerializer):
    """
    User Profile Serializer
    """
    instructor_profile = serializers.SerializerMethodField()

    def get_instructor_profile(self, obj):
        """
        Check that a user has an instructor_profile
        Then check if the instructor_profile is active
        If active, return the instructor_profile id
        """
        try:
            instructor_profile = obj.instructor_profile
            if instructor_profile.is_active:
                return instructor_profile.id
            else:
                return None
        except ObjectDoesNotExist:
            return None

    class Meta:
        model = User

        fields = (
            'id',
            'email',
            'is_active',
            'is_verified',
            'is_staff',
            'instructor_profile',
            'first_name',
            'last_name',
            'gender',
            'avatar',
            'phone_number',
        )

        extra_kwargs = {
            'is_active': {'read_only': True},
            'is_verified': {'read_only': True},
            'is_staff': {'read_only': True},
        }
