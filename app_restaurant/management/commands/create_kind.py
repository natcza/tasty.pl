from django.core.management.base import BaseCommand
# from events.management.commands.create_db import create_organizer

from app_restaurant.models import Restaurant, Kind


class Command(BaseCommand):
    help = "wypełnij kind danymi -- python manage.py create kind"

    def add_arguments(self, parser):
        parser.add_argument('total', nargs=1, type=int, help='Indicates the number of kinds to be created')

    def handle(self, *args, **options):
        total = options['total']
        # id_restaurant = total[0]
        number_kinds = total[0]

        len_kinds = len(Kind.objects.all())
        # jaka jest liczba rekordów w bazie danych

        # sprawdzaj jaki postfix ma ostatni rekord
        # ostatni = Organizer.objects.all()[len_organizers - 1:len_organizers].get().id
        if len_kinds != 0:
            ostatni = Kind.objects.last().id
        else:
            ostatni = 0

        # postfix kolejnej wartości
        # https://docs.python.org/3.9/library/string.html
        # postfix = "{:0>5}".format(str(ostatni + 1))

        print("create_kind")
        for i in range(number_kinds):
            postfix = str("{:0>5}".format(str(ostatni + 1 + i)))
            # print(postfix)
            Kind.objects.create(
                name="kind_" + postfix,
            )
            # section_pk = Section.objects.get(pk=section.id)
            # restaurant_pk = Restaurant.objects.get(pk=id_restaurant)
            # section_pk.restaurants.add(restaurant_pk)

        self.stdout.write(self.style.SUCCESS(f"dopisane {total} rekordów"))