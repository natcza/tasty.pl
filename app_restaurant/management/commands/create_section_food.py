from django.core.management.base import BaseCommand
# from events.management.commands.create_db import create_organizer
import random
from app_restaurant.models import Section, Restaurant, Food


class Command(BaseCommand):
    help = "wypełnij food danymi -- python manage.py create_section"

    def add_arguments(self, parser):
        parser.add_argument('total', nargs=2, type=int, help='Indicates the number of sections to be created')

    def handle(self, *args, **options):
        total = options['total']
        id_sections = total[0]
        number_food = total[1]

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

        len_food = len(Food.objects.all())
        print(len_food)
        # for item_section in range(number_section):
        #     x = random.randint(0, len_section)
        s = list(range(1, len_food+ 1))
        s = random.sample(s, number_food)
        section = Section.objects.get(pk=id_sections)
        for food in s:
            food_pk = Food.objects.get(pk=food)
            food_pk.sections.add(section)
        print(s)


        self.stdout.write(self.style.SUCCESS(f"dopisane {total} rekordów"))
