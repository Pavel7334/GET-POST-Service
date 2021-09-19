from django.db.models import Value, BooleanField
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView
from rest_framework.viewsets import ModelViewSet

from work.models import City, Street, Shop
from work.serializers import CitySerializer, StreetSerializer, ShopSerializer


class CityListAPIView(ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class StreetListAPIView(ListAPIView):
    serializer_class = StreetSerializer

    def get_queryset(self):
        return Street.objects.filter(city_id=self.kwargs['pk'])


class ShopListCreateAPIView(ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['street', 'city', 'open']



