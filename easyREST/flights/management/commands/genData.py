from django.core.management.base import BaseCommand

from flights.models import Flight, Seat, Passenger, Reservation

import random
import datetime

NUM_FLIGHTS_PER_DAY = 5
NUM_DAYS = 30
FLIGHTS = [
    {
        "origin": "LBA",
        "destination": "BHD",
        "travelTime": 70
    },
    {
        "origin": "IPC",
        "destination": "BHD",
        "travelTime": 2000
    },
    {
        "origin": "BHD",
        "destination": "LBA",
        "travelTime": 70
    },
    {
        "origin": "CCU",
        "destination": "DXB",
        "travelTime": 300
    },
    {
        "origin": "DXB",
        "destination": "CCU",
        "travelTime": 300
    },
    {
        "origin": "SYD",
        "destination": "DXB",
        "travelTime": 1500
    },
    {
        "origin": "DXB",
        "destination": "SYD",
        "travelTime": 1500
    }
]

TABLES = [Flight, Seat, Passenger, Reservation]
PLANES = [
    {
        "model": "Concorde",
        "numberOfRows": 5,
        "seatsPerRow": 5,
        "speedMult": 4,
        "seatPrice": 300
    },
    {
        "model": "Private Jet",
        "numberOfRows": 5,
        "seatsPerRow": 2,
        "speedMult": 2,
        "seatPrice": 1000
    },
    {
        "model": "Guppy",
        "numberOfRows": 7,
        "seatsPerRow": 4,
        "speedMult": 0.5,
        "seatPrice": 50
    }
]


class Command(BaseCommand):
    help = "Generates test data"


    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting Old Data...")
        
        for table in TABLES:
            table.objects.all().delete()
        
        self.stdout.write("Generating New Data...")

        self.generate_all_flights()

    #Function to generate a flight with a specific plane
    def generate_flight(self, flight, plane, DepatureDateTime, id):
        flightTime = int(flight["travelTime"] / plane["speedMult"])
        flightID = "MW" + str(id)
        arrivalDateTime = DepatureDateTime + datetime.timedelta(minutes=flightTime)
        flight_data = {
            "flightId": flightID,
            "planeModel": plane["model"],
            "numberOfRows": plane["numberOfRows"],
            "seatsPerRow": plane["seatsPerRow"],
            "departureTime": DepatureDateTime,
            "departureDate": DepatureDateTime.date(),
            "arrivalTime": arrivalDateTime,
            "departureAirport": flight["origin"],
            "destinationAirport": flight["destination"]
        }

        flightInstance = Flight.objects.create(**flight_data)

        total_seats = plane["numberOfRows"] * plane["seatsPerRow"]
        for seatNo in range(total_seats):
            seatID = flightID + str( 1000 + seatNo )
            seat_data = {
                "seatId": seatID,
                "flightId": flightInstance,
                "seatNumber": seatNo,
                "seatPrice": plane["seatPrice"],
                "seatTaken": False
            }
            Seat.objects.create(**seat_data)

        print("Generated Flight ", flightID, " -- From: ", flight["origin"], " -- To: ", flight["destination"], " -- Time of Departure: ", DepatureDateTime.strftime("%m/%d/%Y, %H:%M"))

    
    #Generate a Seed for a Unique ID
    def uniqueid(self):
        seed = random.getrandbits(32)
        while True:
            yield seed
            seed += 1
    
    def generate_all_flights(self):
        unique_ids = self.uniqueid()
        now = datetime.datetime.now()
        today = now.date()

        for days in range(NUM_DAYS):
            flight_date = today + datetime.timedelta(days=days)
            for flights_per_day in range(NUM_FLIGHTS_PER_DAY):
                
                flight = FLIGHTS[random.randint(0,len(FLIGHTS)-1)]
                plane = PLANES[random.randint(0,len(PLANES)-1)]
                flight_time = datetime.time(hour=random.randint(0,23), minute=random.randint(0,59))
                departureDateTime =  datetime.datetime.combine(flight_date, flight_time)
                
                self.generate_flight(flight, plane, departureDateTime, next(unique_ids))