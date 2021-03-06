# Generated by Django 3.2.7 on 2021-09-19 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название города')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
            },
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название улицы')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='work.city', verbose_name='Название города')),
            ],
            options={
                'verbose_name': 'Улица',
                'verbose_name_plural': 'Улицы',
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название магазина')),
                ('house', models.IntegerField(verbose_name='Номер дома')),
                ('opening_time', models.TimeField(verbose_name='Время открытия')),
                ('closing_time', models.TimeField(verbose_name='Время закрытия')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='work.city', verbose_name='Название города')),
                ('street', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='work.street', verbose_name='Название улицы')),
            ],
            options={
                'verbose_name': 'Магазин',
                'verbose_name_plural': 'Магазины',
            },
        ),
    ]
