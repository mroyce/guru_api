import os
import shutil

from django.core.management.base import BaseCommand
from django.conf import settings

from ...models import User
from ...tests.helpers import create_test_user


class Command(BaseCommand):
    """
    gen_dev_data command
    Generate data for our local development environments.
    """
    def handle(self, *args, **kwargs):
        """
        Run gen_dev_data command
        """
        # Only run this command in development environment
        if not settings.DEBUG:
            print 'Only run this in development environment'
            return

        # Delete previous files in `/media/`
        print 'Deleting existing media files'
        folder = settings.MEDIA_ROOT
        if os.path.isdir(folder):
            shutil.rmtree(folder)

        #################### 1. USERS ####################
        print 'Creating Users',

        user_maurice = create_test_user(
            email='maurice@dickinson.edu',
            password='test',
            first_name='Maurice',
            last_name='Royce',
        )
        print '.',

        user_tim = create_test_user(
            email='tim@dickinson.edu',
            password='test',
            first_name='Tim',
            last_name='Kang',
        )
        print '.',

        user_john = create_test_user(
            email='johng307@gmail.com',
            password='test',
            first_name='John',
            last_name='G',
        )
        print '.',

        user_alpha = create_test_user(
            email='alpha@example.com',
            password='test',
            first_name='Alpha',
            last_name='Smith',
        )
        print '.',

        user_bravo = create_test_user(
            email='bravo@example.com',
            password='test',
            first_name='Bravo',
            last_name='Smith',
        )
        print '.'

        #################### FINAL OUTPUT ####################
        print '-------------------- Users --------------------'
        print 'There are {} test users:'.format(User.objects.count())
        for user in User.objects.all():
            print ' * User {}:'.format(user.id)
            print '     - email: {}'.format(user.email)
            print '     - name: {}'.format(user.get_short_name())
