from django.shortcuts import render

import datetime

from rest_framework import viewsets

from flights.models import Flight, Seat, Passenger, Reservation
from flights.serializers import FlightSerializer, SeatSerializer, PassengerSerializer, ReservationSerializer

# Create your views here.


class FlightViewSet(viewsets.ModelViewSet):
   queryset = Flight.objects.all()
   serializer_class = FlightSerializer


class SeatViewSet(viewsets.ModelViewSet):
   queryset = Seat.objects.all()
   serializer_class = SeatSerializer

class PassengerViewSet(viewsets.ModelViewSet):
   queryset = Passenger.objects.all()
   serializer_class = PassengerSerializer

class ReservationViewSet(viewsets.ModelViewSet):
   queryset = Reservation.objects.all()
   serializer_class = ReservationSerializer

