from datetime import datetime, timedelta
from PIL import Image

from guru_api.core.utils import get_pil_image_as_django_content_file
from guru_api.core.models import (User, InstructorProfile, Education, Experience,
                                  Credential, CourseListing, CourseSession)


def create_test_image(filename='test.png', size=(160, 160), color='blue'):
    """
    Create and return a test image as a ContentFile
    """
    image = Image.new('RGBA', size, color)
    image_content_file = get_pil_image_as_django_content_file(image, 'png')
    image_content_file.name = filename
    return image_content_file


def create_test_user(email='test@example.com', password='test', first_name='Test', last_name='User', **kwargs):
    """
    Create and return a test User object
    """
    avatar = create_test_image()

    create_kwargs = {
        'email': email,
        'password': password,
        'first_name': first_name,
        'last_name': last_name,
        'avatar': avatar,
    }

    create_kwargs.update(kwargs)
    return User.objects.create_user(**create_kwargs)


def create_test_instructor_profile(user, **kwargs):
    """
    Create and return a test InstructorProfile object
    """
    create_kwargs = {
        'user': user,
    }

    create_kwargs.update(kwargs)
    return InstructorProfile.objects.create(**create_kwargs)


def create_test_education(instructor_profile, school='Test University', **kwargs):
    """
    Create and return a test Education object
    """
    create_kwargs = {
        'instructor_profile': instructor_profile,
        'school': school,
    }

    create_kwargs.update(kwargs)
    return Education.objects.create(**create_kwargs)


def create_test_experience(instructor_profile, role='Test Role', **kwargs):
    """
    Create and return a test Experience object
    """
    create_kwargs = {
        'instructor_profile': instructor_profile,
        'role': role,
    }

    create_kwargs.update(kwargs)
    return Experience.objects.create(**create_kwargs)


def create_test_credential(instructor_profile, name='Test Credential', **kwargs):
    """
    Create and return a test Credential object
    """
    create_kwargs = {
        'instructor_profile': instructor_profile,
        'name': name,
    }

    create_kwargs.update(kwargs)
    return Credential.objects.create(**create_kwargs)


def create_test_course_listing(instructor_profile, title='Test Course Listing', **kwargs):
    """
    Create and return a test CourseListing object
    """
    create_kwargs = {
        'instructor_profile': instructor_profile,
        'title': title,
    }

    create_kwargs.update(kwargs)
    return CourseListing.objects.create(**create_kwargs)


def create_test_course_session(course_listing, user, fee='50.00', **kwargs):
    """
    """
    # Create date two weeks from now
    date = datetime.today() + timedelta(weeks=2)

    create_kwargs = {
        'course_listing': course_listing,
        'user': user,
        'date': date,
        'fee': fee,
    }

    create_kwargs.update(kwargs)
    return CourseSession.objects.create(**create_kwargs)
