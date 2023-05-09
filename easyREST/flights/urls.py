from django.urls import path, include
from rest_framework import routers

from flights.views import FlightViewSet, SeatViewSet, PassengerViewSet, ReservationViewSet

router = routers.DefaultRouter()
router.register(r'Flight', FlightViewSet)
router.register(r'Seat', SeatViewSet)
router.register(r'Passenger', PassengerViewSet)
router.register(r'Reservation', ReservationViewSet)

urlpatterns = [
   path('', include(router.urls)),
]