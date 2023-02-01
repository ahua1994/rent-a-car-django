from rest_framework import serializers
from datetime import datetime
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
    class Meta:
        model = Reservation
        fields = "__all__"

    def validate_date_range(self, start, end):
        d1 = datetime.strptime(start, "%Y/%m/%d")
        d2 = datetime.strptime(end, "%Y/%m/%d")
        today = datetime.today()
        if (d1 - today) < 0:
            raise serializers.ValidationError(
                "Vehicle must be rented from today onwards.")
        if (d2 - d1) <= 0:
            raise serializers.ValidationError(
                "Vehicles must be rented for atleast one day.")
        return f"{start} to {end} is a valid range"
