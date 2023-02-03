from rest_framework import serializers
# from datetime import datetime, date
from django.utils import timezone
from .models import *


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class ReservationSerializer(serializers.ModelSerializer):
    # start_date = serializers.DateField()
    # end_date = serializers.DateField()

    class Meta:
        model = Reservation
        fields = "__all__"

    def validate(self, data):
        d1 = data["start_date"]
        d2 = data["end_date"]
        today = timezone.now().date()
        print("start", d1, "today", today)
        if d1 < today:
            raise serializers.ValidationError(
                "Vehicle must be rented from today onwards.")
        if d1 >= d2:
            raise serializers.ValidationError(
                "Vehicle must be rented for at least one day.")
        return data
