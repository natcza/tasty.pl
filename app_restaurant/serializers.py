from .models import Restaurant
from .models import Section
from rest_framework import serializers

class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['url', 'name', 'city', 'street']

class SectionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Section
        fields = ['id', 'name']

# class RestaurantDetailSerializer(serializers.ModelSerializer):
# class RestaurantDetailSerializer(serializers.HyperlinkedModelSerializer):
#
#     class Meta:
#         model = Restaurant
#         fields = ['name', 'city', 'street', 'house_number', 'phone_number']