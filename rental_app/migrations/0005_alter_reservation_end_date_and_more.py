# Generated by Django 4.1.5 on 2023-02-02 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental_app', '0004_reservation_end_date_reservation_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='start_date',
            field=models.DateField(),
        ),
    ]
