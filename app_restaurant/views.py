from django.shortcuts import render
from .models import Restaurant, Section
from .serializers import RestaurantSerializer, SectionSerializer
from rest_framework import renderers
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        
        'restaurants': reverse('restaurant-list', request=request, format=format)
    })
class RestaurantsView(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class RestaurantDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class SectionsView(generics.ListCreateAPIView):
    serializer_classs = SectionSerializer
    def list(self, request, *args, **kwargs):
        queryset = Section.objects.filter(restaurants=self.kwargs['pk'])
        serializer = SectionSerializer(queryset, many=True)
        return Response(serializer.data)

