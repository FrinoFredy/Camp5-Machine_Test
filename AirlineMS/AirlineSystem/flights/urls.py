from django.urls import path
from .views import (flight_list, flight_create, delete_flight, edit_flight, search_flight, admin_login,
                    authenticate, homepage, admin_dashboard)

urlpatterns = [
    path('', admin_login, name='admin_login'),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    path('flight_list/', flight_list, name='flight_list'),
    path('search_flight/', search_flight, name='search_flight'),
    path('flight_create/', flight_create, name='flight_create'),
    path('flight/edit/<str:flight_id>/', edit_flight, name='edit_flight'),
    path('flight/delete/<str:flight_id>/', delete_flight, name='delete_flight'),
]
