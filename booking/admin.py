from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Admin)
admin.site.register(SalonOwner)
admin.site.register(Employee)
admin.site.register(Customer)
admin.site.register(HairSalon)
admin.site.register(OpeningHours)
admin.site.register(Service)
admin.site.register(Reservation)
admin.site.register(WorkHours)