from django.contrib import admin
from .models import Flight, Seat, Passenger, Reservation

# Register your models here.
admin.site.register(Flight)
admin.site.register(Seat)
admin.site.register(Passenger)
admin.site.register(Reservation)