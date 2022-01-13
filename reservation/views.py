import datetime
from django.shortcuts import render, HttpResponse
from django .views.generic import ListView, FormView, DeleteView
from django.urls import reverse_lazy
from .models import Table, Reservation
from .forms import AvailabilityForm
from .availability import check_availability


class ReservationList(ListView):
    """
    as staff you can see all the reservations at the front side
    as a user you can only see your own booking(s)
    """
    model = Reservation

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_staff:
            reservation_list = Reservation.objects.all()
            return reservation_list
        else:
            reservation_list = Reservation.objects.filter(user=self
                                                          .request.user)
            return reservation_list


class ReservationView(FormView):
    """
    when filling in the form, if table size within start and end time
    is available the booking will be saved and it confirms
    the booking that user had made, if table is not available you
    get a message that table size is not available
    """
    form_class = AvailabilityForm
    template_name = 'reservation/availability_form.html'

    def form_valid(self, form):
        data = form.cleaned_data
        table_list = Table.objects.filter(table_size=data['table_size'])
        available_tables = []
        for table in table_list:
            if check_availability(table, data['time_start'], data['time_end']):
                available_tables.append(table)
        if len(available_tables) > 0:
            table = available_tables[0]
            reservation = Reservation.objects.create(
                user=self.request.user,
                email=data['email'],
                phone=data['phone'],
                table=table,
                date=datetime.date.today(),
                time_start=data['time_start'],
                time_end=data['time_end']
            )
            reservation.save()
            return HttpResponse(reservation)
        else:
            return HttpResponse('Sorry, this table_size is not available!!')


class CancelReservationView(DeleteView):
    """
    after user confirmed the deleted booking you get
    redirected to page of reservation list where you see
    that booking is deleted from list
    """
    model = Reservation
    template_name = 'reservation/reservation_confirm_delete.html'
    success_url = reverse_lazy('reservation:ReservationList')
