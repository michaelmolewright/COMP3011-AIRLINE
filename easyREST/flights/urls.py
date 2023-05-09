from django.urls import path, include
from rest_framework import routers

from flights.views import FlightViewSet, SeatViewSet, PassengerViewSet, ReservationViewSet, get_flights
router = routers.DefaultRouter()
#router.register(r'flights', FlightViewSet, basename='flight')
router.register(r'Seat', SeatViewSet)
router.register(r'Passenger', PassengerViewSet)
router.register(r'Reservation', ReservationViewSet)
#router.register('flights/query=<str:date>&<str:departureAirport>&<str:destinationAirport>/', get_flights)

urlpatterns = [
   path('', include(router.urls)),
   path('flights/query=<str:date>&<str:departureAirport>&<str:destinationAirport>/', get_flights)
]