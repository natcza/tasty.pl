from django.core.management.base import BaseCommand
# from events.management.commands.create_db import create_organizer

from app_restaurant.models import Restaurant


class Command(BaseCommand):
    help = "wypełnij restaurant danymi -- python manage.py create_restaurant"

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of restaurants to be created')

    def handle(self, *args, **options):
        total = options['total']

        len_restaurants = len(Restaurant.objects.all())

        # sprawdzaj jaki postfix ma ostatni rekord
        # ostatni = Organizer.objects.all()[len_organizers - 1:len_organizers].get().id
        if len_restaurants != 0:
            ostatni = Restaurant.objects.last().id
        else:
            ostatni = 0

        # postfix kolejnej wartości
        # https://docs.python.org/3.9/library/string.html
        # postfix = "{:0>5}".format(str(ostatni + 1))

        print("create_restaurant")
        for i in range(total):
            postfix = str("{:0>5}".format(str(ostatni + 1 + i)))
            # print(postfix)
            Restaurant.objects.create(
                name="restaurant_" + postfix,
                city="city_" + postfix,
                postcode="postecode_" + postfix,
                street="street_" + postfix,
                house_number="house_number_" + postfix,
                phone_number="phone_number_" + postfix,
                gis="gis_" + postfix,
            )

        self.stdout.write(self.style.SUCCESS(f"dopisane {total} rekordów do tabeli Restaurant"))

# poetry run python manage.py create_restaurant 20