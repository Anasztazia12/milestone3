from django.core.management.base import BaseCommand
from core.models import Cafe, Spot

CAFES = [
    {
        'name': 'Prufrock Coffee',
        'address': '23-25 Leather Ln',
        'city': 'London',
        'latitude': 51.5204,
        'longitude': -0.1086,
        'has_power_outlets': True,
        'wifi_speed_mbps': 85,
        'quiet_rating': 3,
    },
    {
        'name': 'Grind Shoreditch',
        'address': '85-86 Old St',
        'city': 'London',
        'latitude': 51.5256,
        'longitude': -0.0877,
        'has_power_outlets': True,
        'wifi_speed_mbps': 100,
        'quiet_rating': 2,
    },
    {
        'name': 'The Watch House',
        'address': '199 Bermondsey St',
        'city': 'London',
        'latitude': 51.5002,
        'longitude': -0.0815,
        'has_power_outlets': False,
        'wifi_speed_mbps': 50,
        'quiet_rating': 4,
    },
    {
        'name': 'Foundation Coffee House',
        'address': '25 Lever St',
        'city': 'Manchester',
        'latitude': 53.4832,
        'longitude': -2.2331,
        'has_power_outlets': True,
        'wifi_speed_mbps': 120,
        'quiet_rating': 5,
    },
    {
        'name': 'Takk Coffee Co.',
        'address': '6 Tariff St',
        'city': 'Manchester',
        'latitude': 53.4818,
        'longitude': -2.2312,
        'has_power_outlets': True,
        'wifi_speed_mbps': 90,
        'quiet_rating': 4,
    },
    {
        'name': 'Ezra & Gil',
        'address': '20 Hilton St',
        'city': 'Manchester',
        'latitude': 53.4827,
        'longitude': -2.2325,
        'has_power_outlets': True,
        'wifi_speed_mbps': 75,
        'quiet_rating': 3,
    },
]


class Command(BaseCommand):
    help = 'Adds the starter list of cafes to the databse'

    def handle(self, *args, **kwargs):
        for cafe_data in CAFES:
            cafe, created = Cafe.objects.get_or_create(
                name=cafe_data['name'],
                defaults=cafe_data,
            )
            if created:
                Spot.objects.create(cafe=cafe, spot_name='Main area', capacity=4)
                self.stdout.write('Added ' + cafe.name)
            else:
                self.stdout.write(cafe.name + ' alredy exists')
