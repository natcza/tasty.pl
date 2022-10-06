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
python manage.py create_restaurant_sections 1 6
python manage.py create_restaurant_sections 2 7
python manage.py create_restaurant_sections 3 5
python manage.py create_restaurant_sections 5 9
python manage.py create_restaurant_sections 6 9
python manage.py create_restaurant_sections 7 9
python manage.py create_restaurant_sections 8 7
python manage.py create_restaurant_sections 9 4
python manage.py create_restaurant_sections 10 3

echo 'stopped'
exit 0


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
