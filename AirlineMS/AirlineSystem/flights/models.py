from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


class Flight(models.Model):
    flight_id = models.CharField(max_length=10, unique=True)
    dep_airport = models.CharField(max_length=100)
    dep_date = models.DateField()
    dep_time = models.TimeField()
    arr_airport = models.CharField(max_length=100)
    arr_date = models.DateField()
    arr_time = models.TimeField()

    def clean(self):
        # Ensure departure date is not in the past
        if self.dep_date < timezone.now().date():
            raise ValidationError('Departure date cannot be in the past.')

        # Ensure arrival date and time are after the departure date and time
        if self.dep_date == self.arr_date and self.dep_time >= self.arr_time:
            raise ValidationError('Arrival time must be after departure time.')
        elif self.arr_date < self.dep_date:
            raise ValidationError('Arrival date cannot be before the departure date.')

    def __str__(self):
        return f"{self.flight_id} - {self.dep_airport} to {self.arr_airport}"
