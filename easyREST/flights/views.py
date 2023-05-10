from django.shortcuts import render


import datetime

from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.decorators import api_view


from flights.models import Flight, Seat, Passenger, Reservation
from flights.serializers import FlightSerializer, SeatSerializer, PassengerSerializer, ReservationSerializer

# Create your views here.


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


    def list(self, date, departureAirport, destinationAirport):
        #date = request.query_params.get('date')
        #departure_airport = request.query_params.get('departureAirport')
        #destination_airport = request.query_params.get('destinationAirport')

        print(date)

        queryset = Flight.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

class SeatViewSet(viewsets.ModelViewSet):
   queryset = Seat.objects.all()
   serializer_class = SeatSerializer

class PassengerViewSet(viewsets.ModelViewSet):
   queryset = Passenger.objects.all()
   serializer_class = PassengerSerializer

class ReservationViewSet(viewsets.ModelViewSet):
   queryset = Reservation.objects.all()
   serializer_class = ReservationSerializer

@api_view(http_method_names=['GET'])
def get_flights(request, date, departureAirport, destinationAirport):
   
   try:
      queryDate = datetime.datetime.strptime(date, "%Y-%m-%d")
   except ValueError:
      Response("Invalid date.", status=400)

   flightSerializer = FlightSerializer
   seatSerializer = SeatSerializer
   flights = Flight.objects.filter(departureDate=queryDate, departureAirport=departureAirport, destinationAirport=destinationAirport)
   
   jsonReturn = flightSerializer(flights, many=True)

   if len(jsonReturn.data) == 0:
      return Response("No flights found for this date and airports!", status=404)
   
   finalJSOn = []
   #Add seats to the JSON return
   for data in jsonReturn.data:
      seats = Seat.objects.filter(flightId=data["flightId"])
      seatJSON = seatSerializer(seats, many=True)

      data["seats"] = seatJSON.data
      finalJSOn.append(data)

   return Response(finalJSOn, status=200)

@api_view(http_method_names=['POST'])
def book_reservation(request):

   #-----------------FLIGHT------------------#
   try:
      flight = Flight.objects.get(flightId = request.data["flightId"])
      flightSerializer = FlightSerializer
      flightJSON = flightSerializer(flight)
   except Flight.DoesNotExist:
      return Response("Flight does not exist", status=400)
   #----------------------------------------#

   #------------------SEAT-------------------#
   try:
      seat = Seat.objects.get( flightId=request.data["flightId"], seatNumber=request.data["seatNumber"], seatTaken=False)
   except Seat.DoesNotExist:
      return Response("Seat does not exist, or it is taken!", status=400)
   #----------------------------------------#

   #--------------PASSENGER----------------#
   passengerSerializer = PassengerSerializer
   new_passenger = passengerSerializer(data=request.data["passenger"])
   if new_passenger.is_valid():
      passenger = new_passenger.save()
   else:
      return Response(new_passenger.errors, status=400)
   #----------------------------------------#

   #---------------RESERVATION----------------#
   reservationSerializer = ReservationSerializer
   reservation_data = request.data
   del reservation_data["seatNumber"]
   reservation_data["seatId"] = seat.seatId
   reservation_data["passengerId"] = passenger.passengerId

   new_reservation = reservationSerializer(data=reservation_data)
   if new_reservation.is_valid():
      reservation = new_reservation.save()
   else:
      return Response(new_reservation.errors, status=400)
   #----------------------------------------#

   
   finalJSON = {}
   finalJSON["reservationId"] = reservation.reservationId
   finalJSON["holdLuggage"] = request.data["holdLuggage"]
   finalJSON["paymentConfirmed"] = request.data["paymentConfirmed"]
   finalJSON["flight"] = flightJSON.data
   finalJSON["passenger"] = request.data["passenger"]
   finalJSON["seatId"] = seat.seatId


   return Response(finalJSON, status=200)

@api_view(http_method_names=['GET'])
def query_reservation(request, reservationId):
   try:
      seat = Seat.objects.get( flightId=request.data["flightId"], seatNumber=request.data["seatNumber"], seatTaken=False)
   except Seat.DoesNotExist:
      return Response("Seat does not exist, or it is taken!", status=400)

   return Response(reservationId)

@api_view(http_method_names=['PUT'])
def update_reservation(request, reservationId):
   return Response(reservationId)

@api_view(http_method_names=['DELETE'])
def delete_reservation(request, reservationId):
   return Response(reservationId)

@api_view(http_method_names=['PUT'])
def confirm_reservation(request, reservationId):
   return Response(reservationId)