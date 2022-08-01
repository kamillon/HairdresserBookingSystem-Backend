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
    path('pracownik/', views.PracownikList.as_view(), name='pracownik'),
    path('pracownik/<int:pk>/', views.PracownikDetail.as_view(), name='pracownik-details'),
    path('wlasciciel/', views.WlascicielList.as_view(), name='wlasciciel'),
    path('wlasciciel/<int:pk>/', views.WlascicielDetail.as_view(), name='wlasciciel-details'),
    path('klient/', views.KlientList.as_view(), name='klient'),
    path('klient/<int:pk>/', views.KlientDetail.as_view(), name='klient-details'),
    path('salon/', views.SalonList.as_view(), name='salon-list'),
    path('salon/<int:pk>/', views.SalonDetail.as_view(), name='salon-details'),
    path('usluga/', views.UslugaList.as_view(), name='usluga-list'),
    path('usluga/<int:pk>/', views.UslugaDetail.as_view(), name='usluga-details'),
    path('reservation/', views.ReservationList.as_view(), name='reservation-list'),
    path('reservation/<int:pk>/', views.ReservationDetail.as_view(), name='reservation-details'),
    path('opening-hours/', views.OpeningHoursList.as_view(), name='opening-hours-list'),
    path('opening-hours/<int:pk>/', views.ReservationDetail.as_view(), name='opening-hours-details'),
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
]
