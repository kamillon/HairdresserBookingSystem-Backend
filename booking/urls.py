from django.urls import path, include
from . import views
from django.contrib import admin
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'booking', views.UserView, 'booking')

admin.site.site_url = 'http://127.0.0.1:8000/'
urlpatterns = [

    # path('api/', include(router.urls)),
    path('user/', views.UserList.as_view(), name='user-list'),
    path('user/<int:pk>/', views.UserDetail.as_view(), name='user-details'),
    # path('pracownik/', views.PracownikList.as_view(), name='pracownik'),
    # path('pracownik/<int:pk>/', views.PracownikDetail.as_view(), name='pracownik-details'),
    # path('wlasciciel/', views.WlascicielList.as_view(), name='wlasciciel'),
    # path('wlasciciel/<int:pk>/', views.WlascicielDetail.as_view(), name='wlasciciel-details'),
    # path('klient/', views.KlientList.as_view(), name='klient'),
    # path('klient/<int:pk>/', views.KlientDetail.as_view(), name='klient-details'),
    path('salon/', views.SalonList.as_view(), name='salon-list'),
    path('salon/<int:pk>/', views.SalonDetail.as_view(), name='salon-details'),
    path('service/', views.ServiceList.as_view(), name='service-list'),
    path('service/<int:pk>/', views.ServiceDetail.as_view(), name='service-details'),
    path('reservation/', views.ReservationList.as_view(), name='reservation-list'),
    path('reservation/<int:pk>/', views.ReservationDetail.as_view(), name='reservation-details'),
    path('opening-hours/', views.OpeningHoursList.as_view(), name='opening-hours-list'),
    path('opening-hours/<int:pk>/', views.OpeningHoursDetail.as_view(), name='opening-hours-details'),
    path('admin-info/', views.AdminList.as_view(), name='admin-info'),
    path('admin-info/<int:pk>/', views.AdminDetail.as_view(), name='admin-info-details'),
    path('salon-owner/', views.SalonOwnerList.as_view(), name='salon-owner'),
    path('salon-owner/<int:pk>/', views.SalonOwnerDetail.as_view(), name='salon-owner-details'),
    path('employee/', views.EmployeeList.as_view(), name='employee'),
    path('employee/<int:pk>/', views.EmployeeDetail.as_view(), name='employee-details'),
    path('customer/', views.CustomerList.as_view(), name='customer'),
    path('customer/<int:pk>/', views.CustomerDetail.as_view(), name='customer-details'),
    path('work-hours/', views.WorkHoursList.as_view(), name='work-hours'),
    path('work-hours/<int:pk>/', views.WorkHoursDetail.as_view(), name='work-hours-details'),
    path('employee-work-hours/<int:pk>/', views.EmployeeWorkHours.as_view(), name='employee-work-hours'),
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
]
