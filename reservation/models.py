from datetime import datetime
from django.db import models
from django.conf import settings
from django.urls import reverse_lazy


class Table(models.Model):
    """
    each table in the restaurant have a table number and it contains
    a table size for the number of persons that can sit at the table
    """
    table_nr = models.IntegerField()
    TABLE_SIZE_LIST = (
        ('two persons', 'TWO PERSONS'),
        ('four persons', 'FOUR PERSONS'),
        ('six persons', 'SIX PERSONS'),
        ('eight persons', 'EIGHT PERSONS'),
    )
    table_size = models.CharField(max_length=15, choices=TABLE_SIZE_LIST)

    def __str__(self):
        return f'tablenumber {self.table_nr} for {self.table_size}'


class Reservation(models.Model):
    """
    all the information that is neccesary to book a table,
    the user needs to be logged in, we need to know the
    date, start time and end time, email and phone for
    contact. When logged in and registered you can also cancel
    the booking yourself
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    email = models.EmailField(default=False)
    phone = models.IntegerField(default=0)
    date = models.DateField(default=datetime.now)
    time_start = models.TimeField(default=datetime.now)
    time_end = models.TimeField(default=datetime.now)

    def __str__(self):
        return f'{self.user} has booked {self.table} at {self.date} \
               from {self.time_start} until {self.time_end})'

    def cancel_reservation_url(self):
        return reverse_lazy('reservation:CancelReservationView',
                            args=[self.pk, ])
