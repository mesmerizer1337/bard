from django.urls import path
from .views import table_list, create_table, available_tables

urlpatterns = [
    path("", table_list, name="table_list"),
    path("create/", create_table, name="create_table"),
    path("available/", available_tables, name="available_tables"),
]
