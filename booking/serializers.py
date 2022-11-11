from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import *

from django.contrib.auth import get_user_model

User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_superuser', 'is_employee',
                  'password', 'phone', 'role', 'is_active']

class UserSerializer(UserSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_superuser', 'is_employee',
                  'phone', 'role', 'is_active']

class SalonSerializer(serializers.ModelSerializer):
    class Meta:
        model = HairSalon
        fields = '__all__'


class UslugaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = ['id', 'customerId', 'salonId', 'serviceId', 'employeeId', 'date', 'start_time', 'end_time', 'is_active']

class OpeningHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningHours
        fields = '__all__'

class UserDeleteSerializer(serializers.Serializer):
    pass


class SalonOwnerSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    class Meta:
        model = SalonOwner
        fields = ('user', 'salary', 'salon', 'image')