from django.db import models

# Create your models here.


class Customer(models.Model):
    def __str__(self):
        return f"Customer {self.pk}"


class Car(models.Model):
    plate_number = models.CharField(max_length=8, unique=True)
    make = models.CharField(max_length=16)
    model = models.CharField(max_length=20)
    year = models.SmallIntegerField()
    daily_rate = models.IntegerField()
    availability = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.make} {self.model} {self.year}"


class Reservation(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    date_created = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, null=True)
    car = models.ForeignKey(Car, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f"{self.car} Reserved {self.start_date} to {self.end_date} by {self.customer}"
