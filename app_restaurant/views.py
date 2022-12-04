from django.shortcuts import render
from .models import Restaurant, Section, Kind
from .serializers import RestaurantSerializer, SectionSerializer, KindSerializer
from rest_framework import renderers
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        
        'restaurants': reverse('restaurant-list', request=request, format=format),
        'kinds': reverse('kind-list', request=request, format=format)
    })
class RestaurantsView(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class KindsView(generics.ListCreateAPIView):
    queryset = Kind.objects.all()
    serializer_class = KindSerializer

class RestaurantDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class SectionsView(generics.ListCreateAPIView):
    serializer_class = SectionSerializer
    queryset = Section
    def get_queryset(self):
        restaurant_pk = self.kwargs['pk']
        return Section.objects.filter(restaurants=restaurant_pk)
