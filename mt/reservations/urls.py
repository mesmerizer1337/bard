from django.urls import path
from .views import (
    reservation_list, reservation_detail, user_reservations,
    create_reservation, update_reservation, delete_reservation
)

urlpatterns = [
    path("", reservation_list, name="reservation_list"),
    path("<int:id>/", reservation_detail, name="reservation_detail"),
    path("user/<int:user_id>/", user_reservations, name="user_reservations"),
    path("create/", create_reservation, name="create_reservation"),
    path("<int:id>/update/", update_reservation, name="update_reservation"),
    path("<int:id>/delete/", delete_reservation, name="delete_reservation"),
    path('create_table/', create_table, name='create_table'),
    path('create_reservation/', create_reservation, name='create_reservation'),
]
