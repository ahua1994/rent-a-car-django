# Generated by Django 4.1.5 on 2023-02-01 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rental_app', '0002_reservation_car_reservation_customer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='start_date',
        ),
    ]