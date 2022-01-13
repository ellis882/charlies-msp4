from django import forms
from .models import Events


class EventForm(forms.ModelForm):
    """
    all the fields from Events.models
    are used for the form at the restaurant website
    """
    class Meta:
        model = Events
        fields = '__all__'
