from rest_framework import serializers

from guru_api.core.models import CourseListing


class CourseListingSerializer(serializers.ModelSerializer):
    """
    CourseListing Model Serializer
    """
    class Meta:
        model = CourseListing

        fields = (
            'id',
            'instructor_profile',
            'title',
            'description',
            'cancellation_fee',
        )
