from django.utils.timezone import now
from rest_framework.fields import SerializerMethodField
from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer

from work.models import Shop, City, Street


class ShopSerializer(ModelSerializer):
    open = SerializerMethodField()
    street = StringRelatedField()
    city = StringRelatedField()

    class Meta:
        model = Shop
        fields = '__all__'

    def get_open(self, obj):
        opening_time = obj.opening_time.strftime('%H:%M:%S')
        closing_time = obj.closing_time.strftime('%H:%M:%S')
        now_time = now().strftime('%H:%M:%S')
        opening_time = list(map(int, opening_time.split(':')))
        closing_time = list(map(int, closing_time.split(':')))
        now_time = list(map(int, now_time.split(':')))
        obj.open = opening_time < now_time < closing_time
        obj.save()
        return obj.open


class CitySerializer(ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class StreetSerializer(ModelSerializer):
    city = StringRelatedField()

    class Meta:
        model = Street
        fields = '__all__'

