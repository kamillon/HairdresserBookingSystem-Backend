from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import generics, permissions, status
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.reverse import reverse

User = get_user_model()

# Create your views here.


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    name = 'user-list'
    permission_classes = [IsAuthenticated]


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    name = 'user-details'
    permission_classes = [IsAuthenticated]


class SalonList(generics.ListCreateAPIView):
    queryset = HairSalon.objects.all()
    serializer_class = SalonSerializer
    name = 'salon-list'
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        qs = HairSalon.objects.all()
        city = self.request.query_params.get('city')
        if city is not None:
            qs = qs.filter(city__iexact=city)
        return qs


class SalonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = HairSalon.objects.all()
    serializer_class = SalonSerializer
    name = 'salon-details'
    permission_classes = [IsAuthenticated]


class ServiceList(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    name = 'service-list'
    permission_classes = [IsAuthenticatedOrReadOnly]


class ServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    name = 'service-details'
    permission_classes = [IsAuthenticated]


class ReservationList(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    name = 'reservation-list'
    permission_classes = [IsAuthenticatedOrReadOnly]


class ReservationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    name = 'reservation-details'
    permission_classes = [IsAuthenticated]


class ReservationAllInformation(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationAllSerializer
    name = 'reservation-all-information'
    permission_classes = [IsAuthenticated]


class OpeningHoursList(generics.ListCreateAPIView):
    queryset = OpeningHours.objects.all()
    serializer_class = OpeningHoursSerializer
    name = 'opening-hours-list'
    permission_classes = [IsAuthenticated]


class OpeningHoursDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OpeningHours.objects.all()
    serializer_class = OpeningHoursSerializer
    name = 'opening-hours-details'
    permission_classes = [IsAuthenticated]


class AdminList(generics.ListCreateAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    name = 'admin-info'
    permission_classes = [IsAuthenticated]


class AdminDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    name = 'admin-info-details'
    permission_classes = [IsAuthenticated]


class SalonOwnerList(generics.ListCreateAPIView):
    queryset = SalonOwner.objects.all()
    serializer_class = SalonOwnerSerializer
    name = 'salon-owner'
    permission_classes = [IsAuthenticated]


class SalonOwnerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SalonOwner.objects.all()
    serializer_class = SalonOwnerSerializer
    name = 'salon-owner-details'
    permission_classes = [IsAuthenticated]


class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    name = 'employee'
    permission_classes = [IsAuthenticatedOrReadOnly]


class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    name = 'employee-details'
    permission_classes = [IsAuthenticated]


class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    name = 'customer'
    permission_classes = [IsAuthenticated]


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    name = 'customer-details'
    permission_classes = [IsAuthenticated]


class WorkHoursList(generics.ListCreateAPIView):
    queryset = WorkHours.objects.all()
    serializer_class = WorkHoursSerializer
    name = 'work-hours'
    permission_classes = [IsAuthenticated]


class WorkHoursDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkHours.objects.all()
    serializer_class = WorkHoursSerializer
    name = 'work-hours-details'
    permission_classes = [IsAuthenticated]


class EmployeeWorkHours(generics.ListAPIView):
    serializer_class = WorkHoursSerializer
    name = 'employee-work-hours'
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        slug = self.kwargs['pk']
        queryset = WorkHours.objects.filter(employeeId=slug)
        if queryset:
            return queryset
        else:
            raise NotFound()


class ListOfOwnersSalons(generics.ListAPIView):
    serializer_class = ListOfOwnersSalonsSerializer
    name = 'list-of-owners-salons'
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        slug = self.kwargs['pk']
        queryset = HairSalon.objects.filter(owner=slug)
        if queryset:
            return queryset
        else:
            raise NotFound()


class ListOpeningHours(generics.ListAPIView):
    serializer_class = ListOpeningHours
    name = 'list-opening-hours'
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        slug = self.kwargs['pk']
        queryset = OpeningHours.objects.filter(salonId=slug)
        if queryset:
            return queryset
        else:
            raise NotFound()


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({'allUserList': reverse(UserList.name, request=request),
                         'salon': reverse(SalonList.name, request=request),
                         'service': reverse(ServiceList.name, request=request),
                         'reservation': reverse(ReservationList.name, request=request),
                         'reservationAll': reverse(ReservationAllInformation.name, request=request),
                         'openingHours': reverse(OpeningHoursList.name, request=request),
                         'admin': reverse(AdminList.name, request=request),
                         'salonOwner': reverse(SalonOwnerList.name, request=request),
                         'employee': reverse(EmployeeList.name, request=request),
                         'customer': reverse(CustomerList.name, request=request),
                         'workHours': reverse(WorkHoursList.name, request=request),
                         'employeeWorkHours': "http://127.0.0.1:8000/employee-work-hours/1",
                         'listOfOwnersSalons': "http://127.0.0.1:8000/list-of-owners-salons/1",
                         'listOpeningHours': "http://127.0.0.1:8000/list-opening-hours/1",
                         })
