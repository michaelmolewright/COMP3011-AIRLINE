from django.shortcuts import render


import datetime

from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.decorators import action


from flights.models import Flight, Seat, Passenger, Reservation
from flights.serializers import FlightSerializer, SeatSerializer, PassengerSerializer, ReservationSerializer

# Create your views here.


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


    def list(self, date, departureAirport, destinationAirport):
        #date = request.query_params.get('date')
        #departure_airport = request.query_params.get('departureAirport')
        #destination_airport = request.query_params.get('destinationAirport')

        print(date)

        queryset = Flight.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

class SeatViewSet(viewsets.ModelViewSet):
   queryset = Seat.objects.all()
   serializer_class = SeatSerializer

class PassengerViewSet(viewsets.ModelViewSet):
   queryset = Passenger.objects.all()
   serializer_class = PassengerSerializer

class ReservationViewSet(viewsets.ModelViewSet):
   queryset = Reservation.objects.all()
   serializer_class = ReservationSerializer

def get_flights(self, date, departureAirport, destinationAirport):
        #date = request.query_params.get('date')
        #departure_airport = request.query_params.get('departureAirport')
        #destination_airport = request.query_params.get('destinationAirport')

        print(date)

        queryset = Flight.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)