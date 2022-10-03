from django.core.management.base import BaseCommand
# from events.management.commands.create_db import create_organizer

from app_restaurant.models import Section, Restaurant


class Command(BaseCommand):
    help = "wypełnij restaurant danymi -- python manage.py create_section"

    def add_arguments(self, parser):
        parser.add_argument('total', nargs=1, type=int, help='Indicates the number of sections to be created')

    def handle(self, *args, **options):
        total = options['total']
        # id_restaurant = total[0]
        number_sections = total[0]

        len_sections = len(Section.objects.all())

        # sprawdzaj jaki postfix ma ostatni rekord
        # ostatni = Organizer.objects.all()[len_organizers - 1:len_organizers].get().id
        if len_sections != 0:
            ostatni = Section.objects.last().id
        else:
            ostatni = 0

        # postfix kolejnej wartości
        # https://docs.python.org/3.9/library/string.html
        # postfix = "{:0>5}".format(str(ostatni + 1))

        print("create_restaurant")
        for i in range(number_sections):
            postfix = str("{:0>5}".format(str(ostatni + 1 + i)))
            # print(postfix)
            Section.objects.create(
                name="section_" + postfix,
            )
            # section_pk = Section.objects.get(pk=section.id)
            # restaurant_pk = Restaurant.objects.get(pk=id_restaurant)
            # section_pk.restaurants.add(restaurant_pk)

        self.stdout.write(self.style.SUCCESS(f"dopisane {total} rekordów"))

# poetry run python manage.py create_section 20