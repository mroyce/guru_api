from django.conf import settings
from django.core.management import call_command
from django.core.management.base import NoArgsCommand


class Command(NoArgsCommand):
    help = "Bootstrap the database in a development environment."

    def handle(self, *args, **kwargs):
        """
        Carry out the boostrap command
        """
        # Only run this command in development environment
        if not settings.DEBUG:
            print 'Only run this in development environment'
            return

        BOOTSTRAP_COMMANDS = [
            # Run Migrations
            ('migrate', (), {'interactive': False}),

            # Flush Data
            ('flush', (), {'interactive': False}),

            # Load Dev Data
            ('gen_dev_data', (), {}),
        ]

        # Run all commands
        for c, cargs, ckwargs in BOOTSTRAP_COMMANDS:
            kw = ckwargs.copy()
            kw.update(kwargs)
            print 'Running', c, '...'
            call_command(c, *cargs, **kw)
            print 'Done running', c
