from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)


class User(AbstractUser):
    USER_TYPE = [
        ("admin", "admin"),
        ("customer", "klient"),
        ("employee", "pracownik"),
        ("salon_owner", "właścieciel salonu"),
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
        return self.email


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='admin', primary_key=True)
    # image = models.ImageField(upload_to=upload_to, blank=True, null=True, default='default.jpg')

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer', primary_key=True)
    # image = models.ImageField(upload_to=upload_to, blank=True, null=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


class SalonOwner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='salon_owner', primary_key=True)
    # image = models.ImageField(upload_to=upload_to, blank=True, null=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name



class HairSalon(models.Model):
    name = models.CharField(max_length=50, unique=False)
    city = models.CharField(max_length=100, blank=False, null=False)
    street = models.CharField(max_length=100, unique=False)
    house_number = models.CharField(max_length=5, unique=False)
    post_code = models.CharField(max_length=20, blank=True, null=True)
    postal_code_locality = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=9, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    owner = models.ForeignKey(SalonOwner, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "HairSalons"


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee', primary_key=True)
    salon = models.ForeignKey(HairSalon, null=True, on_delete=models.CASCADE)
    # image = models.ImageField(upload_to=upload_to, blank=True, null=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


class OpeningHours(models.Model):
    WEEKDAYS = [
        (1, _("Monday")),
        (2, _("Tuesday")),
        (3, _("Wednesday")),
        (4, _("Thursday")),
        (5, _("Friday")),
        (6, _("Saturday")),
        (0, _("Sunday")),
    ]

    salonId = models.ForeignKey(HairSalon, on_delete=models.CASCADE)
    weekday = models.IntegerField(choices=WEEKDAYS, unique=False)
    from_hour = models.TimeField(blank=True, null=True, unique=False)
    to_hour = models.TimeField(blank=True, null=True, unique=False)
    is_closed = models.BooleanField(default=False)


class Service(models.Model):
    SERVICE_TYPE = [
        ("women's", "Damskie"),
        ("men's", "Meskie"),
    ]

    name = models.CharField(max_length=100, unique=False)
    service_type = models.CharField(choices=SERVICE_TYPE, max_length=20)
    describe = models.TextField(blank=True, null=True)
    #czas okreslony w minutach
    time = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    salonID = models.ForeignKey(HairSalon, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Services"


class Reservation(models.Model):
    customerId = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customerId_reservation')
    salonId = models.ForeignKey(HairSalon, on_delete=models.CASCADE, related_name='salonId_reservation')
    serviceId = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='serviceId_reservation')
    date = models.DateField(null=False, blank=False, unique=False)
    start_time = models.TimeField(blank=True, null=True, unique=False)
    end_time = models.TimeField(blank=True, null=True, unique=False)
    employeeId = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='employeeId_reservation')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.id

    class Meta:
        verbose_name_plural = "Reservations"

    def __unicode__(self):
        return str(self.data) + " User: " + str(self.customerId)

    # def is_active(self):
    #     now = datetime.now().date()
    #     if now > self.date and self.is_active:
    #         self.active = False
    #         self.save()
    #         return False
    #     return self.is_active

    # @property
    # def is_active(self):
    #     return datetime.now().date() < self.date

    @property
    def is_active(self):
        now = datetime.now().date()
        if now > self.date:
            return False
        return True

class WorkHours(models.Model):
    WEEKDAYS = [
        (1, _("Monday")),
        (2, _("Tuesday")),
        (3, _("Wednesday")),
        (4, _("Thursday")),
        (5, _("Friday")),
        (6, _("Saturday")),
        (0, _("Sunday")),
    ]
    employeeId = models.ForeignKey(Employee, on_delete=models.CASCADE)
    weekday = models.IntegerField(choices=WEEKDAYS, unique=False)
    from_hour = models.TimeField(null=True, blank=True, unique=False)
    to_hour = models.TimeField(null=True, blank=True, unique=False)
    is_day_off = models.BooleanField(null=True, default=False)

    def __str__(self):
        return self.id


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == 'admin':
            Admin.objects.create(user=instance)
        elif instance.role == 'salon_owner':
            SalonOwner.objects.create(user=instance)
        elif instance.role == 'employee':
            Employee.objects.create(user=instance)
        elif instance.role == 'customer':
            Customer.objects.create(user=instance)


@receiver(post_save, sender=HairSalon)
def create_opening_hours(sender, instance, created, **kwargs):
    if created:
        for x in range(0, 7):
            OpeningHours.objects.create(salonId=instance, weekday=x)


@receiver(post_save, sender=Employee)
def create_work_hours(sender, instance, created, **kwargs):
    if created:
        for x in range(0, 7):
            WorkHours.objects.create(employeeId=instance, weekday=x)
