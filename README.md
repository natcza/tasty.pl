# tasty.pl
mkdocs serve -a localhost:8008
http://localhost:8008/

endpoint dla głównego katalogu API 
--> API root
# Food
lista food jest związana z określoną restauracją

# Sekcja
sekcja jest związana z określoną restauracją

03.10.2022
Done:
wpisane rekordy restauracji i sekcji do bazy danych. 
dopisanie do danej restauracji (pk.restaurant) listy sekcji.

ToDo:
- seralizer Sekcji

class SectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Section
        fields = ['name']

- widok sekcji do danej restuaracji (pk.restaurant) --> crud sekcji (creat new section, read, update, delete) do pk.restaurant
Jakie sekcje ma podana restauracja?

# kind
- dla każda restauracja może być skojarzona z określoną listą kind


