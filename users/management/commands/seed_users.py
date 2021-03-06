from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User

"""
django_seed required
1) install : pipenv django_seed
2) register : "django_seed" at "settings.py"
"""
# ⭐️ command : python manage.py seed_users --number 50

NAME = "users"


class Command(BaseCommand):

    help = f"This command creates {NAME}"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", type=int, help=f"How many {NAME} do you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        seeder.add_entity(
            User,
            number,
            {
                "is_staff": False,
                "is_superuser": False,
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} {NAME} created!"))
