from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import EventForm
from .models import EventImage


def event_reservation_form(request):
    """
    form that user filles in when want to book an event
    at the restaurant. When form is valid form is saved
    and get a succes message. Info goes to backend so that
    restaurant manager can contact the user.
    """
    event_form = EventForm()

    if request.method == 'POST':
        event_form = EventForm(request.POST)

        if event_form.is_valid():
            event_form.save()
            return redirect('events:send_success')

    context = {'form': event_form}

    return render(request, 'events/event.html', context)


def send_success(request):
    return HttpResponse('Thanks for your email we will contact you soon!')


def event_images(request):
    event_image = list(EventImage.objects.all())

    context = {
        'event_image': event_image
    }

    return render(request, 'events/event.html', context)
