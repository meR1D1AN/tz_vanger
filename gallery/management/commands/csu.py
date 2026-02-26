import os

from django.contrib.auth.models import User
from django.core.management import BaseCommand


class Command(BaseCommand):
    """Создание суперпользователя"""

    def handle(self, *args, **options):
        username = os.getenv('ADMIN_LOGIN')
        email = os.getenv('ADMIN_EMAIL')
        password = os.getenv('ADMIN_PASS')

        if not User.objects.filter(username=username).exists() and not User.objects.filter(email=email).exists():
            user = User.objects.create_superuser(
                username=username,
                email=email,
            )
            user.set_password(password)
            user.save()

            self.stdout.write(self.style.SUCCESS(f'=== ADMIN с логином {username} успешно создан ==='))
        else:
            self.stdout.write(
                self.style.WARNING(f'!!! ADMIN с логином {username} или email {email} уже существует !!!')
            )
