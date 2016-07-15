from rest_framework import serializers

from guru_api.core.models import InstructorProfile, Education, Experience, Credential


class EducationSerializer(serializers.ModelSerializer):
    """
    Education Model Serializer
    """
    class Meta:
        model = Education

        fields = (
            'school',
            'year_started',
            'year_ended',
            'degree_type',
            'field_of_study',
            'grade',
            'description',
        )


class ExperienceSerializer(serializers.ModelSerializer):
    """
    Experience Model Serializer
    """
    class Meta:
        model = Experience

        fields = (
            'role',
            'organization',
            'year_started',
            'year_ended',
            'description',
        )


class CredentialSerializer(serializers.ModelSerializer):
    """
    Credential Model Serializer
    """
    class Meta:
        model = Credential

        fields = (
            'name',
            'description',
        )



class InstructorProfileSerializer(serializers.ModelSerializer):
    """
    Instructor Model Serializer
    """
    education = EducationSerializer(many=True, required=False)
    experience = ExperienceSerializer(many=True, required=False)
    credentials = CredentialSerializer(many=True, required=False)

    class Meta:
        model = InstructorProfile

        fields = (
            'id',
            'biography',
            'website',
            'will_travel',
            'trial_lesson',
            'education',
            'experience',
            'credentials',
            'course_listings',
        )
