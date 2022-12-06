from .models import Restaurant, Section, Kind
from rest_framework import serializers


# class KindSerializer(serializers.ModelSerializer):
class KindSerializer(serializers.HyperlinkedModelSerializer):
    # restaurants = serializers.PrimaryKeyRelatedField(queryset=Restaurant.objects.all(), many=True)
    # restaurants = serializers.HyperlinkedRelatedField(queryset=Restaurant.objects.all(), many=True, view_name='restaurant-detail')
    # url = serializers.CharField(source='get_absolute_url', read_only=True)
    # view_name = 'kind'
    restaurants = serializers.SlugRelatedField(queryset=Restaurant.objects.all(), many=True,
                                                      slug_field='name')
    # restaurants = serializers.PrimaryKeyRelatedField(queryset=Restaurant.objects.all(), many=True)
    # view_name='kind-detail'
    class Meta:
        model = Kind
        fields = ['id', 'name', 'restaurants']

class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    kind_list = KindSerializer(many=True, read_only=True)

    class Meta:
        model = Restaurant
        fields = ['url', 'name', 'city', 'street', 'house_number', 'phone_number', 'kind_list']


class SectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Section
        fields = ['name']
