from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions, status
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.reverse import reverse

User = get_user_model()


# class UserView(viewsets.ModelViewSet):
#     serializer_class = UserCreateSerializer
#     queryset = User.objects.all()
#     permission_classes = [IsAuthenticated]
#





# Create your views here.

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    name = 'user-list'


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    name = 'user-details'


class SalonList(generics.ListCreateAPIView):
    queryset = Salon.objects.all()
    serializer_class = SalonSerializer
    name = 'salon-list'
    # permission_classes = [IsAuthenticated]

class SalonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Salon.objects.all()
    serializer_class = SalonSerializer
    name = 'salon-details'
    # permission_classes = [IsAuthenticated]



class UslugaList(generics.ListCreateAPIView):
    queryset = Usluga.objects.all()
    serializer_class = UslugaSerializer
    name = 'usluga-list'
    # permission_classes = [IsAuthenticated]

class UslugaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usluga.objects.all()
    serializer_class = UslugaSerializer
    name = 'usluga-details'
    # permission_classes = [IsAuthenticated]


class ReservationList(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    name = 'reservation-list'
    # permission_classes = [IsAuthenticated]

class ReservationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    name = 'reservation-details'
    # permission_classes = [IsAuthenticated]


class OpeningHoursList(generics.ListCreateAPIView):
    queryset = OpeningHours.objects.all()
    serializer_class = OpeningHoursSerializer
    name = 'opening-hours-list'
    # permission_classes = [IsAuthenticated]

class OpeningHoursDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OpeningHours.objects.all()
    serializer_class = OpeningHoursSerializer
    name = 'opening-hours-details'
    # permission_classes = [IsAuthenticated]





class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({'pracownicy': reverse(UserList.name, request=request),
                         'salon': reverse(SalonList.name, request=request),
                         'usluga': reverse(UslugaList.name, request=request),
                         'reservation': reverse(ReservationList.name, request=request),
                         'openingHours': reverse(OpeningHoursList.name, request=request),
                         })