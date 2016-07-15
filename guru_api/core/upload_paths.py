import os
import uuid

from django.conf import settings


class UploadPath(object):
    """
    Class based approach for building dynamic file paths for uploaded media files.
    """
    def __init__(self, directory_prefix):
        """
        Constructor
        Args:
            directory_prefix => The directory that the image will be uploaded to
                                (i.e. 'profile-picture', 'identity-picture')
        """
        self.directory_prefix = directory_prefix

    def __call__(self, instance, filename):
        """
        Returns the path to upload the media content to
        Args:
            instance => An instance of we are building the path for (i.e. User, Group, AnonymousIdentity)
            filename => The final name for the uploaded file.
        """
        # Get the file extension, e.g. '.png'
        current_filename, file_extension = os.path.splitext(filename)
        
        # Generate a new filename, using uuid to generate a random unique id
        upload_filename = '{}{}'.format(str(uuid.uuid1()), file_extension)

        # Return the full path
        return self._build_full_path(instance, upload_filename)

    def _build_full_path(self, instance, upload_filename):
        """
        Build the full path for the file to be uploaded to
        i.e. `/media/upload/users/3/profile-picture/{uuid}.png`
        """
        # Get the appropriate `id` from the instance
        id = getattr(instance, 'id')

        # Construct full path
        return '{upload_root}{directory_prefix}/{id}/{filename}'.format(
            upload_root=settings.UPLOAD_ROOT,
            id=str(id),
            directory_prefix=self.directory_prefix,
            filename=upload_filename
        )

    def deconstruct(self):
        """
        Needed for django migrations:
        https://docs.djangoproject.com/en/1.8/topics/migrations/#custom-deconstruct-method
        """
        return ('guru_api.core.upload_paths.UploadPath', [self.directory_prefix], {})


user_upload_path = UploadPath('users')
