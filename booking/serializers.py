from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import *

from django.contrib.auth import get_user_model

User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_superuser', 'is_employee',
                  'password', 'phone', 'role']


class SalonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salon
        fields = '__all__'


class UslugaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usluga
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = ['id', 'klientID', 'salonID', 'uslugaID', 'do_kogo', 'data', 'godzina', 'is_active']

class OpeningHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningHours
        fields = '__all__'