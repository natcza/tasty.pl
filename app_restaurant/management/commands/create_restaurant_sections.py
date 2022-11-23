from django.core.management.base import BaseCommand
# from events.management.commands.create_db import create_organizer
import random
from app_restaurant.models import Section, Restaurant

"""
poetry run python manage.py create_restaurant_sections 18 10

"""

class Command(BaseCommand):
    help = "wypełnij restaurant danymi -- python manage.py create_section"

    def add_arguments(self, parser):
        parser.add_argument('total', nargs=2, type=int, help='Indicates the number of sections to be created')

    def handle(self, *args, **options):
        total = options['total']
        id_restaurant = total[0]
        number_section = total[1]

        # len_sections = len(Section.objects.all())

        # sprawdzaj jaki postfix ma ostatni rekord
        # ostatni = Organizer.objects.all()[len_organizers - 1:len_organizers].get().id
        # if len_sections != 0:
        #     ostatni = Section.objects.last().id
        # else:
        #     ostatni = 0

        # postfix kolejnej wartości
        # https://docs.python.org/3.9/library/string.html
        # postfix = "{:0>5}".format(str(ostatni + 1))

        # print("create_restaurant")
        # for i in range(number_section):
        #     postfix = str("{:0>5}".format(str(ostatni + 1 + i)))
        #     # print(postfix)
        #     Section.objects.create(
        #         name="section_" + postfix,
        #     )
            # section_pk = Section.objects.get(pk=section.id)
            # restaurant_pk = Restaurant.objects.get(pk=id_restaurant)
            # section_pk.restaurants.add(restaurant_pk)

        len_section = len(Section.objects.all())
        print(len_section)
        # for item_section in range(number_section):
        #     x = random.randint(0, len_section)
        s = list(range(1, len_section + 1))
        s = random.sample(s, number_section)
        restaurant = Restaurant.objects.get(pk=id_restaurant)
        for section in s:
            section_pk = Section.objects.get(pk=section)
            section_pk.restaurants.add(restaurant)
        print(s)


        self.stdout.write(self.style.SUCCESS(f"dopisane {total} rekordów"))

# poetry run python manage.py create_restaurant_sections 1 5