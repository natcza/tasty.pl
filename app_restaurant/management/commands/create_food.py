from django.core.management.base import BaseCommand
# from events.management.commands.create_db import create_organizer

from app_restaurant.models import Food


class Command(BaseCommand):
    help = "wypełnij food danymi -- python manage.py create_food
    def add_arguments(self, parser):
        parser.add_argument('total', nargs=1, type=int, help='Indicates the number of food to be created')

    def handle(self, *args, **options):
        total = options['total']
        # id_restaurant = total[0]
        number_food = total[0]

        len_food = len(Food.objects.all())

        # sprawdzaj jaki postfix ma ostatni rekord
        # ostatni = Organizer.objects.all()[len_organizers - 1:len_organizers].get().id
        if len_food != 0:
            ostatni = Food.objects.last().id
        else:
            ostatni = 0

        # postfix kolejnej wartości
        # https://docs.python.org/3.9/library/string.html
        # postfix = "{:0>5}".format(str(ostatni + 1))

        print("create_restaurant")
        for i in range(number_food):
            postfix = str("{:0>5}".format(str(ostatni + 1 + i)))
            # print(postfix)
            Food.objects.create(
                name="food_" + postfix,
                price = i,

            )
            # section_pk = Section.objects.get(pk=section.id)
            # restaurant_pk = Restaurant.objects.get(pk=id_restaurant)
            # section_pk.restaurants.add(restaurant_pk)

        self.stdout.write(self.style.SUCCESS(f"dopisane {total} rekordów w tabeli Food"))

# poetry run python manage.py create_food