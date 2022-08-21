# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Reservation
from .serializers import ReservationSerializer
from api import serializers
# from .utils import getNoteList, createNote, getNotedetail, updateNote, deleteNote

@api_view(['GET']) 
def getRoutes(request):

    routes = [
        {
            'Endpoint': '/reservations/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/reservations/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single reservation object'
        },
        {
            'Endpoint': '/reservations/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new reservation with data sent in post request'
        },
        {
            'Endpoint': '/reservations/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing reservation with data sent in post request'
        },
        {
            'Endpoint': '/reservations/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting reservation'
        },
    ]
    return Response(routes)

# /notes GET
# /notes POST
# /notes/<id> GET
# /notes/<id> PUT
# /notes/<id> DELETE

# @api_view(['GET', 'POST'])
@api_view(['GET', 'POST'])
def getReservations(request):

    if request.method == 'GET':
        reservations = Reservation.objects.all()
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data)
        # return getNoteList(request)

    if request.method == 'POST':
        data = request.data
        reservation = Reservation.objects.create(
            # body=data['body']
            Exhibit=data['Exhibit'],
            Day=data['Day'],
            Time=data['Time'],
        )
        serializer = ReservationSerializer(reservation, many=False)
        return Response(serializer.data)
#         return createNote(request)

# @api_view(['GET', 'PUT', 'DELETE'])
@api_view(['GET'])
def getReservation(request, pk):

    if request.method == 'GET':
        reservations = Reservation.objects.get(id=pk)
        serializer = ReservationSerializer(reservations, many=False)
        return Response(serializer.data)
        return getNotedetail(request, pk)

    # if request.method == 'PUT':
    #     return updateNote(request, pk)

    # if request.method == 'DELETE':
    #     return deleteNote(request, pk)