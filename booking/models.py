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


class HairSalon(models.Model):
    name = models.CharField(max_length=50, unique=True)
    city = models.CharField(max_length=100, blank=False, null=False)
    street = models.CharField(max_length=100, unique=True)
    house_number = models.CharField(max_length=5, unique=True)
    post_code = models.CharField(max_length=20, blank=True, null=True)
    postal_code_locality = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=9, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "HairSalons"



class Service(models.Model):
    SERVICE_TYPE = [
        ("women's", "Damskie"),
        ("men's", "Meskie"),
    ]

    name = models.CharField(max_length=100, unique=True)
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


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    image = models.ImageField(upload_to=upload_to, blank=True, null=True, default='default.jpg')


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee')
    salary = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    salon = models.ForeignKey(HairSalon, null=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_to, blank=True, null=True, default='default.jpg')


class SalonOwner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='salon_owner', primary_key=True)
    salary = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    salon = models.ForeignKey(HairSalon, null=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_to, blank=True, null=True, default='default.jpg')


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='admin')
    image = models.ImageField(upload_to=upload_to, blank=True, null=True, default='default.jpg')


class Reservation(models.Model):
    customerId = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customerId_reservation')
    salonId = models.ForeignKey(HairSalon, on_delete=models.CASCADE, related_name='salonId_reservation')
    serviceId = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='serviceId_reservation')
    date = models.DateField(null=False, blank=False)
    start_time = models.TimeField()
    end_time = models.TimeField()
    employeeId = models.ForeignKey(User, on_delete=models.CASCADE, related_name='employeeId_reservation')
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.id

    class Meta:
        verbose_name_plural = "Reservations"

    def __unicode__(self):
        return str(self.data) + " User: " + str(self.customerId)


class WorkHours(models.Model):
    employeeId = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField(null=False, blank=False)
    from_hour = models.TimeField(null=True, blank=True)
    to_hours = models.TimeField(null=True, blank=True)
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
