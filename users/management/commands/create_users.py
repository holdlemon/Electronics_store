from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist


class Command(BaseCommand):
    """Создание тестовых пользователей: один активный, другой неактивный"""

    def handle(self, *args, **options):
        User = get_user_model()

        # Тестовый пользователь 1 (активный)
        try:
            User.objects.get(username="test1").delete()
        except ObjectDoesNotExist:
            pass

        user1 = User.objects.create(
            username="test1",
            is_active=True,
            is_staff=True,
        )
        user1.set_password("12345qwert")
        user1.save()
        self.stdout.write(
            self.style.SUCCESS(
                f"Активный пользователь - сотрудник создан: {user1.username}"
            )
        )

        # Тестовый пользователь 2 (НЕактивный)
        try:
            User.objects.get(username="test2").delete()
        except ObjectDoesNotExist:
            pass

        user2 = User.objects.create(
            username="test2",
            is_active=True,
        )
        user2.set_password("12345qwert")
        user2.save()
        self.stdout.write(
            self.style.SUCCESS(
                f"Активный пользователь - НЕсотрудник создан: {user2.username}"
            )
        )
