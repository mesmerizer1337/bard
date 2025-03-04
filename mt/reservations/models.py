from django.db import models
from django.core.exceptions import ValidationError
from customers.models import Customer
from tables.models import Table

class Reservation(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("canceled", "Canceled"),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")

    def clean(self):
        """ Validation for reservations """
        existing_reservation = Reservation.objects.filter(
            table=self.table, date=self.date
        ).exclude(id=self.id)
        if existing_reservation.exists():
            raise ValidationError("This table is already reserved for the selected date.")
        
        user_reservations = Reservation.objects.filter(
            customer=self.customer, date=self.date
        ).exclude(id=self.id)
        if user_reservations.exists():
            raise ValidationError("The user already has a reservation on this day.")

    def save(self, *args, **kwargs):
        self.clean()  # Run validation before saving
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Reservation {self.id} - {self.customer.name} - {self.date} - {self.status}"
