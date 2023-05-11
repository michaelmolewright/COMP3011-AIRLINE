from django.test import TestCase

# Create your tests here.
bookingTest = {
  "passenger": {
    "firstName": "John",
    "lastName": "Doe",
    "dateOfBirth": "2000-01-23",
    "passportNumber": "832494168",
    "address": "23 Woodhouse Lane"
  },
  "flightId": "MW2759663477",
  "holdLuggage": true,
  "paymentConfirmed": false,
  "seatNumber": 3
}

bookingTest = {
  "passenger": {
    "firstName": "John",
    "lastName": "Doe",
    "dateOfBirth": "2000-01-23",
    "passportNumber": "832494168",
    "address": "23 Woodhouse Lane"
  },
  "flightId": "MW2759663477",
  "holdLuggage": true,
  "paymentConfirmed": false,
  "seatNumber": 3
}

{
    "reservationId": 3,
    "holdLuggage": true,
    "paymentConfirmed": false,
    "flight": {
        "flightId": "MW2759663477",
        "planeModel": "Guppy",
        "numberOfRows": 7,
        "seatsPerRow": 4,
        "departureTime": "2023-06-07T02:12:00",
        "arrivalTime": "2023-06-09T04:12:00",
        "departureAirport": "DXB",
        "destinationAirport": "SYD"
    },
    "passenger": {
        "firstName": "John",
        "lastName": "Doe",
        "dateOfBirth": "2000-01-23",
        "passportNumber": "832494168",
        "address": "23 Woodhouse Lane"
    },
    "seatId": "MW27596634771003"
}