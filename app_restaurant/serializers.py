from .models import Restaurant, Section, Kind
from rest_framework import serializers

class KindSerializer(serializers.ModelSerializer):
    restaurants = serializers.PrimaryKeyRelatedField(queryset=Restaurant.objects.all(), many=True)
    class Meta:
        model = Kind
        fields = ('id', 'name', 'restaurants')

class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    kind_list = KindSerializer(many=True, read_only=True)
    class Meta:
        model = Restaurant
        fields = ['url', 'name', 'city', 'street', 'house_number', 'phone_number', 'kind_list']

class SectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Section
        fields = ['name']