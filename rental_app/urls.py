from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path("cars/", CarView.as_view()),
    path("reservation/add", ReservationView.as_view()),
    path("reservations/", ReservationRUDView.as_view()),
]
