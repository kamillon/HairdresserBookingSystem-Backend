# Generated by Django 4.0.5 on 2022-11-11 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_alter_user_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='user',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='salon',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='user',
        ),
        migrations.RemoveField(
            model_name='hairsalon',
            name='owner',
        ),
        migrations.DeleteModel(
            name='OpeningHours',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='customerId',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='employeeId',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='salonId',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='serviceId',
        ),
        migrations.RemoveField(
            model_name='salonowner',
            name='salon',
        ),
        migrations.RemoveField(
            model_name='salonowner',
            name='user',
        ),
        migrations.RemoveField(
            model_name='service',
            name='salonID',
        ),
        migrations.RemoveField(
            model_name='workhours',
            name='employeeId',
        ),
        migrations.DeleteModel(
            name='Admin',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.DeleteModel(
            name='HairSalon',
        ),
        migrations.DeleteModel(
            name='Reservation',
        ),
        migrations.DeleteModel(
            name='SalonOwner',
        ),
        migrations.DeleteModel(
            name='Service',
        ),
        migrations.DeleteModel(
            name='WorkHours',
        ),
    ]