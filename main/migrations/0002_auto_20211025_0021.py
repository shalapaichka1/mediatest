# Generated by Django 3.2.8 on 2021-10-24 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='closeTime',
            field=models.TimeField(verbose_name='Время закрытия'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='openTime',
            field=models.TimeField(verbose_name='Время открытия'),
        ),
    ]