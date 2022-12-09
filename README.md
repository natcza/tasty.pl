# tasty.pl
2022.12.09
/Combine List
{
    "restaurant-count" : resteaurant-count,
    "restaurants" : restaurant.data,
    "kind-count" : kind-count,
    "kinds" : kind.data
}



endpoint dla głównego katalogu API 
--> API root

# Sekcje

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

