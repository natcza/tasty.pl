from django.shortcuts import render

# Create your views here.
from django.views import generic
from rest_framework import generics
from .models import Restaurant
from .serializers import RestaurantSerializer

class RestaurantsView(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class RestaurantDetailView(generic.DetailView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer