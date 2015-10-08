import os
import uuid

from django.conf import settings


class UploadPath(object):
    """
    Class based approach for building dynamic file paths for uploaded media files.
    https://docs.djangoproject.com/en/1.8/ref/models/fields/#django.db.models.FileField.upload_to
    """
    def __init__(self, model_name, directory_prefix):
        """
        Constructor
        Args:
            model_name => The name of the model we are saving the media file for
                          (i.e. 'user', 'membership')
            directory_prefix => The directory that the image will be uploaded to
                                (i.e. 'profile-picture', 'identity-picture')
        """
        self.model_name = model_name
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
        i.e. `/media/upload/user/3/profile-picture/{uuid}.png`
        """
        # Get the appropriate `id` from the instance
        id = getattr(instance, 'id')

        # Construct full path
        return '{upload_root}{model_name}/{id}/{directory_prefix}/{filename}'.format(
            upload_root=settings.UPLOAD_ROOT,
            model_name=self.model_name,
            id=str(id),
            directory_prefix=self.directory_prefix,
            filename=upload_filename
        )

    def deconstruct(self):
        """
        Needed for django migrations:
        https://docs.djangoproject.com/en/1.8/topics/migrations/#custom-deconstruct-method
        """
        return ('django_rest_skeleton.core.upload_paths.UploadPath', [self.model_name, self.directory_prefix], {})
