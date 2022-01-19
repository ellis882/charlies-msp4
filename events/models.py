from django.db import models


class Events(models.Model):
    """
    info required to manage events from backend
    when user wants to book an event at the restaurant
    with this info restaurant manager can contact
    user for organizing the event
    """
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    event = (
          ('private party', 'PRIVATE PARTY'),
          ('birthday party', 'BIRTHDAY PARTY'),
          ('Diner and movie', 'DINER AND MOVIE')
    )
    type_of_event = models.CharField(max_length=50, choices=event)
    number_of_persons = models.IntegerField()
    Date_of_event = models.DateField()
    message = models.TextField(max_length=1000)

    class Meta:
        verbose_name = 'events'
        verbose_name_plural = 'events'

    def __str__(self):
        return str(self.name)


class EventImage(models.Model):
    event_type = models.CharField(max_length=50)
    image = models.ImageField(upload_to='event/')

    class Meta:
        verbose_name = 'event_image'
        verbose_name_plural = 'event_image'

    def __str__(self):
        return str(self.event_type)
