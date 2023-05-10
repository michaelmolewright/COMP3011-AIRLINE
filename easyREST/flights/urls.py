from django.urls import path, include
from rest_framework import routers

from flights.views import FlightViewSet, SeatViewSet, PassengerViewSet, ReservationViewSet, get_flights, book_reservation, query_reservation, update_reservation, delete_reservation, confirm_reservation
router = routers.DefaultRouter()
#router.register(r'flights', FlightViewSet, basename='flight')
router.register(r'Seat', SeatViewSet)
router.register(r'Passenger', PassengerViewSet)
router.register(r'Reservation', ReservationViewSet)
#router.register('flights/query=<str:date>&<str:departureAirport>&<str:destinationAirport>/', get_flights)

urlpatterns = [
   path('', include(router.urls)),
   path('flights/query=<str:date>&<str:departureAirport>&<str:destinationAirport>/', get_flights),
   path('res/book/', book_reservation),
   path('res/query=<str:reservationId>/', query_reservation),
   path('res/update/query=<str:reservationId>/', update_reservation),
   path('res/delete/query=<str:reservationId>/', delete_reservation),
   path('res/confirm/query=<str:reservationId>/', confirm_reservation),

]