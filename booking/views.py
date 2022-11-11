from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions, status
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.parsers import MultiPartParser, FormParser

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
    queryset = HairSalon.objects.all()
    serializer_class = SalonSerializer
    name = 'salon-list'
    # permission_classes = [IsAuthenticated]

class SalonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = HairSalon.objects.all()
    serializer_class = SalonSerializer
    name = 'salon-details'
    # permission_classes = [IsAuthenticated]



class UslugaList(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = UslugaSerializer
    name = 'usluga-list'
    # permission_classes = [IsAuthenticated]

class UslugaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
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


class PracownikList(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    name = 'pracownik'
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = User.objects.filter(role="employee")
        if queryset:
            return queryset
        else:
            raise NotFound()

class PracownikDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    name = 'pracownik-details'
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = User.objects.filter(role="employee")
        if queryset:
            return queryset
        else:
            raise NotFound()

class WlascicielList(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    name = 'wlasciciel'
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = User.objects.filter(role="salon_owner")
        if queryset:
            return queryset
        else:
            raise NotFound()

class WlascicielDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    name = 'wlasciciel-details'
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = User.objects.filter(role="salon_owner")
        if queryset:
            return queryset
        else:
            raise NotFound()

class KlientList(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    name = 'klient'
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = User.objects.filter(role="customer")
        if queryset:
            return queryset
        else:
            raise NotFound()

class KlientDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    name = 'klient-details'
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = User.objects.filter(role="customer")
        if queryset:
            return queryset
        else:
            raise NotFound()


class SalonOwnerList(generics.ListCreateAPIView):
    queryset = SalonOwner.objects.all()
    serializer_class = SalonOwnerSerializer
    name = 'salon-owner'
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]


class SalonOwnerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SalonOwner.objects.all()
    serializer_class = SalonOwnerSerializer
    name = 'salon-owner-details'
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({'pracownicy': reverse(UserList.name, request=request),
                         'salon': reverse(SalonList.name, request=request),
                         'usluga': reverse(UslugaList.name, request=request),
                         'reservation': reverse(ReservationList.name, request=request),
                         'openingHours': reverse(OpeningHoursList.name, request=request),
                         'salonOwner': reverse(SalonOwnerList.name, request=request),
                         'pracownik': reverse(PracownikList.name, request=request),
                         'wlasciciel': reverse(WlascicielList.name, request=request),
                         'klient': reverse(KlientList.name, request=request),
                         })