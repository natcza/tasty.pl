from django.shortcuts import render

# Create your views here.
# from django.views import generic

from .models import Restaurant
from .serializers import RestaurantSerializer

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

