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
    {
        'name': 'Strangers Coffee House',
        'address': '21 Wensum St',
        'city': 'Norwich',
        'latitude': 52.6321,
        'longitude': 1.2965,
        'has_power_outlets': True,
        'wifi_speed_mbps': 65,
        'quiet_rating': 3,
    },
    {
        'name': 'The Birdcage',
        'address': '23 Pottergate',
        'city': 'Norwich',
        'latitude': 52.6304,
        'longitude': 1.2937,
        'has_power_outlets': False,
        'wifi_speed_mbps': 40,
        'quiet_rating': 4,
    },
    {
        'name': 'Costa Coffee (Belvaros)',
        'address': '1 Regent Rd',
        'city': 'Great Yarmouth',
        'latitude': 52.6076,
        'longitude': 1.7305,
        'has_power_outlets': True,
        'wifi_speed_mbps': 55,
        'quiet_rating': 3,
        'members_only': False,
    },
    {
        'name': 'Starbucks Coffee (Market Gates)',
        'address': '31 Market Gates',
        'city': 'Great Yarmouth',
        'latitude': 52.6067,
        'longitude': 1.7280,
        'has_power_outlets': True,
        'wifi_speed_mbps': 50,
        'quiet_rating': 2,
        'members_only': True,
    },
    {
        'name': 'The Vault',
        'address': '156 High St',
        'city': 'Gorleston-on-Sea',
        'latitude': 52.5763,
        'longitude': 1.7256,
        'has_power_outlets': False,
        'wifi_speed_mbps': 45,
        'quiet_rating': 4,
        'members_only': True,
    },
    {
        'name': 'Starbucks Coffee (Gapton Hall)',
        'address': 'Gapton Hall Rd',
        'city': 'Great Yarmouth',
        'latitude': 52.5930,
        'longitude': 1.7057,
        'has_power_outlets': True,
        'wifi_speed_mbps': 50,
        'quiet_rating': 2,
        'members_only': True,
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
