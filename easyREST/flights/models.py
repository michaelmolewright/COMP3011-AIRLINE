from django.db import models

# Create your models here.


class Flight(models.Model):
    flight_id = models.CharField(primary_key=True, max_length=10)
    plane_model = models.CharField(max_length=100)
    number_of_rows = models.IntegerField()
    seats_per_row = models.IntegerField()
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    origin = models.CharField(max_length=5)
    destination = models.CharField(max_length=5)


class Seat(models.Model):
    seat_id = models.AutoField(primary_key=True)
    flight_id = models.ForeignKey(Flight, on_delete=models.CASCADE)
    seat_number = models.IntegerField()
    seat_price = models.DecimalField(max_digits=10, decimal_places=2)

class Passenger(models.Model):
    passenger_id = models.CharField(primary_key=True, max_length=10)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    DOB = models.DateField()
    passport_number = models.IntegerField()
    address = models.CharField(max_length=100)

class Reservation(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    seat_id = models.ForeignKey(Seat, on_delete=models.CASCADE)
    passenger_id = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    hold_luggage = models.BooleanField()
    payment_confirmed = models.BooleanField()