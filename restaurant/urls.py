"""restaurant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_restaurant import views
from app_restaurant.views import (
    RestaurantsView,
    RestaurantDetailView,
    SectionsView,
    KindsView,
    CombineListView,
)
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.api_root),
    path('restaurants/', RestaurantsView.as_view(), name='restaurant-list'),
    path('kinds/', KindsView.as_view(), name='kind-list'),
    path('restaurants/<int:pk>', RestaurantDetailView.as_view(), name='restaurant-detail'),
    path('restaurants/<int:pk>/sections/', SectionsView.as_view(), name='section-list'),
    path('combines/', CombineListView.as_view(), name='combine-list')
]

urlpatterns = format_suffix_patterns(urlpatterns)
