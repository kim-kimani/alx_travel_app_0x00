from django.core.management.base import BaseCommand
from listings.models import Listing
import random

class Command(BaseCommand):
    help = 'Seed database with sample listings'

    def handle(self, *args, **kwargs):
        locations = ["Paris", "New York", "Tokyo", "London", "Dubai", "Sydney", "Rome"]
        titles = ["Cozy Apartment", "Luxury Villa", "Beach House", "Modern Loft", "Mountain Cabin"]

        for i in range(20):
            title = f"{random.choice(titles)} in {random.choice(locations)}"
            description = f"A beautiful place to stay while visiting {title.split(' in ')[1]}"
            location = title.split(" in ")[1]
            price_per_night = round(random.uniform(50, 500), 2)

            Listing.objects.create(
                title=title,
                description=description,
                location=location,
                price_per_night=price_per_night
            )
            self.stdout.write(self.style.SUCCESS(f'Seeded: {title}'))

        self.stdout.write(self.style.SUCCESS('Successfully seeded listings'))