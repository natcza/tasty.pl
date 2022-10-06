from django.core.management.base import BaseCommand
# from events.management.commands.create_db import create_organizer
import random
from app_restaurant.models import Restaurant, Kind


class Command(BaseCommand):
    help = "wypełnij relację restaurant-kind danymi -- python manage.py create_restaurant_kind"

    def add_arguments(self, parser):
        parser.add_argument('total', nargs=2, type=int, help='Indicates the number of restaurant_kind to be created')

    def handle(self, *args, **options):
        total = options['total']
        id_restaurant = total[0]
        number_kind = total[1]

        len_kind = len(Kind.objects.all())
        print(len_kind)
 
        s = list(range(1, len_kind + 1))
        s = random.sample(s, number_kind)
        restaurant = Restaurant.objects.get(pk=id_restaurant)
        for kind in s:
            kind_pk = Kind.objects.get(pk=kind)
            kind_pk.restaurants.add(restaurant)
        print(s)

        self.stdout.write(self.style.SUCCESS(f"dopisane {total} rekordów"))
