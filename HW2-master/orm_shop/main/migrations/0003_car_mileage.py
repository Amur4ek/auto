# Generated by Django 3.2.24 on 2024-02-24 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_car_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='mileage',
            field=models.SmallIntegerField(default=300),
            preserve_default=False,
        ),
    ]
