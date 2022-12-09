from django.shortcuts import render
from .models import Restaurant, Section, Kind
from .serializers import (
    RestaurantSerializer,
    SectionSerializer,
    KindSerializer,
    CombineSerializer,
    KindOnlySerializer,
    RestaurantOnlySerializer,
)
from rest_framework import renderers
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from itertools import chain


@api_view(['GET'])
def api_root(request, format=None):
    return Response({

        'restaurants': reverse('restaurant-list', request=request, format=format),
        'kinds': reverse('kind-list', request=request, format=format),
        'combines': reverse('combine-list', request=request, format=format)
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


class CombineListView(generics.ListCreateAPIView):
    # queryset = Restaurant.objects.all()

    # serializer_class = CombineSerializer

    def get_serializer_class(self):
        # print("--------------------request: ", self.request)
        return RestaurantOnlySerializer



    def list(self, request, *args, **kwargs):
        restaurant = Restaurant.objects.all()
        serializer_restaurant = RestaurantOnlySerializer(restaurant, many=True)
        kind = Kind.objects.all()
        serializer_kind = KindOnlySerializer(kind, many=True)

        return Response({
            "restaturant-count" : Restaurant.objects.all().count(),
            "restaurants": serializer_restaurant.data,
            "kind-count" : Kind.objects.all().count(),
            "kinds": serializer_kind.data
        })
