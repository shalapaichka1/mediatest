# Generated by Django 3.2.8 on 2021-10-24 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, verbose_name='Город')),
                ('house_number', models.PositiveSmallIntegerField(verbose_name='Дом')),
                ('openTime', models.TimeField(verbose_name='время открытия')),
                ('closeTime', models.TimeField(verbose_name='время закрытия')),
            ],
            options={
                'verbose_name': 'Магазин',
                'verbose_name_plural': 'Магазины',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_name', models.CharField(max_length=70, verbose_name='Город')),
                ('shops', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='street', to='main.shop', verbose_name='Магазины')),
            ],
            options={
                'verbose_name': 'Улица',
                'verbose_name_plural': 'Улицы',
                'ordering': ['street_name'],
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=50, verbose_name='Город')),
                ('streets', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='city', to='main.street', verbose_name='Улицы')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
                'ordering': ['city_name'],
            },
        ),
    ]
