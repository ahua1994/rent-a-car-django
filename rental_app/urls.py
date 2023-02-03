from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path("cars/", CarView.as_view()),
    path("reservation/add/", ReservationView.as_view()),
    path("reservation/<int:pk>", ReservationRUDView.as_view()),
]
