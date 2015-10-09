from PIL import Image

from ..utils import get_pil_image_as_django_content_file
from ..models import User


def create_test_user(email='test@example.com', password='test', first_name='Test', last_name='User', **kwargs):
    """
    Create and return a test User object
    """
    create_kwargs = {
        'email': email,
        'password': password,
        'first_name': first_name,
        'last_name': last_name,
    }
    create_kwargs.update(kwargs)
    return User.objects.create_user(**create_kwargs)


def create_test_image(filename='test.png', size=(160, 160), color='green'):
    """
    Create and return a test image as a ContentFile
    """
    image = Image.new('RGBA', size, color)
    image_content_file = get_pil_image_as_django_content_file(image, 'png')
    image_content_file.name = filename
    return image_content_file
