from django.db import models

# Create your models here.


class Flight(models.Model):
    flightId  = models.CharField(primary_key=True, max_length=100)
    planeModel = models.CharField(max_length=100)
    numberOfRows = models.IntegerField()
    seatsPerRow = models.IntegerField()
    departureTime = models.DateTimeField()
    departureDate = models.DateField()
    arrivalTime = models.DateTimeField()
    departureAirport = models.CharField(max_length=5)
    destinationAirport = models.CharField(max_length=5)


class Seat(models.Model):
    seatId = models.CharField(primary_key=True, max_length=100)
    flightId = models.ForeignKey(Flight, on_delete=models.CASCADE)
    seatNumber = models.IntegerField()
    seatPrice = models.IntegerField()
    seatTaken = models.BooleanField(default=False)

class Passenger(models.Model):
    passengerId = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    dateOfBirth = models.DateField()
    passportNumber = models.IntegerField()
    address = models.CharField(max_length=100)

class Reservation(models.Model):
    reservationId = models.AutoField(primary_key=True)
    seatId = models.ForeignKey(Seat, on_delete=models.CASCADE)
    passengerId = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    holdLuggage = models.BooleanField(default=False)
    paymentConfirmed = models.BooleanField(default=False)
