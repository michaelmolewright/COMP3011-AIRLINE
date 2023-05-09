from django.core.management.base import BaseCommand

from flights.models import Flight, Seat, Passenger, Reservation

import random
import datetime

NUM_FLIGHTS_PER_DAY = 10
NUM_DAYS = 30

class Command(BaseCommand):
    help = "Generates test data"


    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")

        