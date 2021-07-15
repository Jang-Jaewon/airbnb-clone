from django.core.management.base import BaseCommand
from rooms.models import Facility


# ⭐️ command : python manage.py seed_facilities

NAME = "facilities"


class Command(BaseCommand):

    help = f"This command creates {NAME}"

    def handle(self, *args, **options):
        facilities = [
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]
        for i in facilities:
            Facility.objects.create(name=i)
        self.stdout.write(self.style.SUCCESS(f"{len(facilities)} {NAME} created!"))
