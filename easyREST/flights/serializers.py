from rest_framework import serializers

from flights.models import Flight, Seat, Passenger, Reservation


class FlightSerializer(serializers.ModelSerializer):
   class Meta:
       model = Flight
       fields = ('flightId', 'planeModel', 'numberOfRows',
                 'seatsPerRow', 'departureTime', 'arrivalTime',
                 'departureAirport', 'destinationAirport')


class SeatSerializer(serializers.ModelSerializer):
   class Meta:
       model = Seat
       fields = ('seatId', 'flightId', 'seatNumber', 'seatPrice', 'seatTaken')

class PassengerSerializer(serializers.ModelSerializer):
   class Meta:
       model = Passenger
       fields = ('firstName', 'lastName', 'dateOfBirth',
                 'passportNumber', 'address')

class ReservationSerializer(serializers.ModelSerializer):
   class Meta:
       model = Reservation
       fields = ('reservationId', 'seatId', 'passengerId',
                 'holdLuggage', 'paymentConfirmed')