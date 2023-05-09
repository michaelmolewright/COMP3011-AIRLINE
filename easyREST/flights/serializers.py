from rest_framework import serializers

from flights.models import Flight, Seat, Passenger, Reservation


class FlightSerializer(serializers.ModelSerializer):
   class Meta:
       model = Flight
       fields = ('flight_id', 'plane_model', 'number_of_rows',
                 'seats_per_row', 'departure_time', 'arrival_time',
                 'origin', 'destination')


class SeatSerializer(serializers.ModelSerializer):
   class Meta:
       model = Seat
       fields = ('seat_id', 'flight_id', 'seat_number', 'seat_price')

class PassengerSerializer(serializers.ModelSerializer):
   class Meta:
       model = Passenger
       fields = ('passenger_id', 'first_name', 'last_name', 'DOB',
                 'passport_number', 'address')

class ReservationSerializer(serializers.ModelSerializer):
   class Meta:
       model = Reservation
       fields = ('reservation_id', 'seat_id', 'passenger_id',
                 'hold_luggage', 'payment_confirmed')