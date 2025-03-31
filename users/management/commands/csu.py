from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Кастомная команда создания суперпользователя"""

    def handle(self, *args, **options):
        User = get_user_model()
        try:
            User.objects.get(username="admin").delete()
        except ObjectDoesNotExist:
            pass
        user = User.objects.create(
            username="admin",
        )
        user.set_password("12345qwert")
        user.is_staff = True
        user.is_superuser = True
        user.save()
        self.stdout.write(
            self.style.SUCCESS(f"Успешно создан суперпользователь с username {user.username}")
        )
