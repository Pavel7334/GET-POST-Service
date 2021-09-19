from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название магазина')
    city = models.ForeignKey('City', on_delete=models.PROTECT, verbose_name='Название города')
    street = models.ForeignKey('Street', on_delete=models.PROTECT, verbose_name='Название улицы')
    house = models.IntegerField(verbose_name='Номер дома')
    opening_time = models.TimeField(verbose_name='Время открытия')
    closing_time = models.TimeField(verbose_name='Время закрытия')
    open = models.BooleanField(verbose_name='Статус открытия', default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'


class City(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название города')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class Street(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название улицы')
    city = models.ForeignKey('City', on_delete=models.PROTECT, verbose_name='Название города')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Улица'
        verbose_name_plural = 'Улицы'
