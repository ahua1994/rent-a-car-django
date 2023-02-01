from django.shortcuts import render
from .serializers import *
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView, ListAPIView
from .models import *

# Create your views here.


class ReservationView(CreateAPIView):
    queryset = Reservation
    serializer_class = ReservationSerializer


class ReservationRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Reservation
    serializer_class = ReservationSerializer


# class CustomerView(ListCreateAPIView):
#     queryset = Customer
#     serializer_class = CustomerSerializer


class CarView(ListAPIView):
    queryset = Car
    serializer_class = CarSerializer
