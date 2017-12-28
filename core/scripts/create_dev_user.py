import django
django.setup()

from django.contrib.auth.models import User
from django.conf import settings


def run():
    if not settings.DEV_ENV:
        print(
            'Don\'t set the dev superuser outside of the dev environment'
            'Create the superuser manually in production.'
        )
        return

    admin = User(username='admin')
    admin.set_password('adminpass123')
    admin.is_superuser = True
    admin.is_staff = True
    admin.save()