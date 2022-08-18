# aby plik był wykonywalny
# chmod +x fill.sh

# uruchamianie skryptu
#./fill.sh
# -----------------------------------------------


#migracja
python manage.py migrate


# utwórz 10 restauracji
python manage.py create_restaurant 10

# uwtórz 20 sekcji
python manage.py create_section 20

# dopisz sekcje do restauracji (relacja ManyToMany)
python manage.py create_restaurant_section 1 6
python manage.py create_restaurant_section 2 7
python manage.py create_restaurant_section 3 5
python manage.py create_restaurant_section 5 9
python manage.py create_restaurant_section 6 9
python manage.py create_restaurant_section 7 9
python manage.py create_restaurant_section 8 7
python manage.py create_restaurant_section 9 4
python manage.py create_restaurant_section 10 3

# utwórz food
python manage.py create_food 20

# dopisz food do sekcji (relacja ManyToMany)
python manage.py creat_section_food 1 5
python manage.py creat_section_food 2 7
python manage.py creat_section_food 3 6
python manage.py creat_section_food 4 8
python manage.py creat_section_food 5 6

# utwórz kind
python manage.py create_kind 20

# dopisz kind do restauracji (relacja ManyToMany)
python manage.py create_restaurant_kind 1 5
python manage.py create_restaurant_kind 2 5
python manage.py create_restaurant_kind 3 5
python manage.py create_restaurant_kind 4 5
python manage.py create_restaurant_kind 5 5
python manage.py create_restaurant_kind 6 5
