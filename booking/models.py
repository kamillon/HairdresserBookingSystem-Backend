from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    USER_TYPE = [
        ("admin", "admin"),
        ("user", "klient"),
        ("employee", "pracownik"),
        ("manager", "właścieciel salonu"),
    ]

    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    phone = models.CharField(null=True, max_length=255)
    is_staff = models.BooleanField(null=True)
    is_superuser = models.BooleanField(null=True)
    is_employee = models.BooleanField(null=True)
    role = models.CharField(choices=USER_TYPE, max_length=20)
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'phone', 'is_staff', 'is_superuser', 'is_employee', 'role']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.username



class OpeningHours(models.Model):
    WEEKDAYS = [
        (1, _("Monday")),
        (2, _("Tuesday")),
        (3, _("Wednesday")),
        (4, _("Thursday")),
        (5, _("Friday")),
        (6, _("Saturday")),
        (7, _("Sunday")),
    ]

    weekday = models.IntegerField(choices=WEEKDAYS)
    from_hour = models.TimeField()
    to_hour = models.TimeField()

    class Meta:
        ordering = ('weekday', 'from_hour')
        unique_together = ('weekday', 'from_hour', 'to_hour')

    def __unicode__(self):
        return u'%s: %s - %s' % (self.get_weekday_display(),
                                 self.from_hour, self.to_hour)

# class OpeningHours(models.Model):
#     store = models.ForeignKey("StoreModel")
#     weekday_from = models.PositiveSmallIntegerField(choices=WEEKDAYS, unique=True)
#     weekday_to = models.PositiveSmallIntegerField(choices=WEEKDAYS)
#     from_hour = models.PositiveSmallIntegerField(choices=HOUR_OF_DAY_24)
#     to_hour = models.PositiveSmallIntegerField(choices=HOUR_OF_DAY_24)
#
#     def get_weekday_from_display(self):
#         return WEEKDAYS[self.weekday_from]
#
#     def get_weekday_to_display(self):
#         return WEEKDAYS[self.weekday_to]

# class SpecialDays(models.Model):
#     holiday_date = models.DateField()
#     closed = models.BooleanField(default=True)
#     from_hour = models.PositiveSmallIntegerField(choices=HOUR_OF_DAY_24, null=True, blank=True)
#     to_hour = models.PositiveSmallIntegerField(choices=HOUR_OF_DAY_24, null=True, blank=True)


class Salon(models.Model):
    nazwa = models.CharField(max_length=50, unique=True)
    miejscowosc = models.CharField(max_length=100, unique=True, blank=False, null=False)
    ulica = models.CharField(max_length=100, unique=True)
    nr_budynku = models.CharField(max_length=5, unique=True)
    kod_pocztowy = models.CharField(max_length=20, blank=True, null=True)
    poczta = models.CharField(max_length=100, blank=True, null=True)
    telefon = models.CharField(max_length=9, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    wlasciciel = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nazwa
    class Meta:
        verbose_name_plural = "Salony"



class Usluga(models.Model):
    RODZAJ_USLUGI = [
        ("Fryzjerskie", "Fryzjerskie"),
        ("Kosmetyczne", "Kosmetyczne"),
        ("Barber", "Barber"),
    ]

    TYP_USLUGI = [
        ("Damskie", "Damskie"),
        ("Meskie", "Meskie"),
    ]

    rodzaj_uslugi = models.CharField(choices=RODZAJ_USLUGI, max_length=20)
    typ_uslugi = models.CharField(choices=TYP_USLUGI, max_length=20)
    nazwa_uslugi = models.CharField(max_length=100, unique=True)
    opis = models.TextField()
    #czas okreslony w minutach
    czas = models.IntegerField(default=0)
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    salonID = models.ForeignKey(Salon, on_delete=models.CASCADE)

    def __str__(self):
        return self.nazwa_uslugi

    class Meta:
        verbose_name_plural = "Uslugi"


class Reservation(models.Model):
    klientID = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client_reservation')
    salonID = models.ForeignKey(Salon, on_delete=models.CASCADE)
    uslugaID = models.ForeignKey(Usluga, on_delete=models.CASCADE)
    data = models.DateTimeField(null=False, blank=False)
    godzina = models.TimeField()
    do_kogo = models.ForeignKey(User, on_delete=models.CASCADE, related_name='employee_reservation')
    is_active = models.BooleanField(default=False)


    def __str__(self):
        return self.id

    class Meta:
        verbose_name_plural = "Rezerwacje"

    def __unicode__(self):
        return str(self.data) + " User: " + str(self.klientID)



