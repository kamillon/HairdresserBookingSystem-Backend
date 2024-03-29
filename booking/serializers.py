from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import *

from django.contrib.auth import get_user_model

User = get_user_model()


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_superuser',
                  'password', 'phone', 'role', 'is_active']


class UserSerializer(UserSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_superuser',
                  'phone', 'role', 'is_active']


class SalonSerializer(serializers.ModelSerializer):
    class Meta:
        model = HairSalon
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = ['id', 'customerId', 'salonId', 'serviceId',
                  'employeeId', 'date', 'start_time', 'end_time', 'is_active',
                  'phone', 'email', 'price']


class OpeningHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningHours
        fields = '__all__'


class UserDeleteSerializer(serializers.Serializer):
    pass


class AdminSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Admin
        fields = '__all__'


class SalonOwnerSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = SalonOwner
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    user = UserCreateSerializer(required=True)

    class Meta:
        model = Employee
        fields = ('salon', 'user')

    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details of employee
        :return: returns a successfully created employee record
        """
        user_data = validated_data.pop('user')
        user = UserCreateSerializer.create(UserCreateSerializer(), validated_data=user_data)
        user.is_active = True
        user.save(update_fields=["is_active"])
        employee, created = Employee.objects.update_or_create(user=user,
                                                              salon=validated_data.pop('salon'))
        return employee


class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Customer
        fields = '__all__'


class WorkHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkHours
        fields = '__all__'


class ListOfOwnersSalonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HairSalon
        fields = '__all__'


class ListOpeningHours(serializers.ModelSerializer):
    class Meta:
        model = OpeningHours
        fields = '__all__'


class ReservationAllSerializer(serializers.ModelSerializer):
    customerId = CustomerSerializer()
    salonId = SalonSerializer()
    serviceId = ServiceSerializer()
    employeeId = EmployeeSerializer()

    class Meta:
        model = Reservation
        fields = ['id', 'customerId', 'salonId', 'serviceId',
                  'employeeId', 'date', 'start_time', 'end_time', 'is_active']


class ListOfSalonCustomers(serializers.ModelSerializer):
    customerId = CustomerSerializer()
    class Meta:
        model = Reservation
        fields = ['customerId']
