from django.urls import path

from work.views import CityListAPIView, StreetListAPIView, ShopListCreateAPIView

urlpatterns = [
    path('city/', CityListAPIView.as_view(), name='city_list'),
    path('city/<int:pk>/street/', StreetListAPIView.as_view(), name='street_list'),
    path('shop/', ShopListCreateAPIView.as_view(), name='shop_list_and_create'),
]
