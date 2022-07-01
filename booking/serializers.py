from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import *

from django.contrib.auth import get_user_model

User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_superuser', 'is_employee',
                  'password', 'phone']


class SalonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salon
        fields = '__all__'


class UslugaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usluga
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    # get_employee = serializers.SerializerMethodField(User.objects.filter(is_employee=True))

    class Meta:
        model = Reservation
        fields = ['id', 'klientID', 'salonID', 'uslugaID', 'data', 'godzina', 'is_active', 'get_employee']

class OpeningHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningHours
        fields = '__all__'