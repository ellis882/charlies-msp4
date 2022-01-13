from django import forms


class AvailabilityForm(forms.Form):
    """
    the required information that is needed
    to book a table when user fills in the
    booking form with input format
    """
    email = forms.EmailField(required=True)
    phone = forms.IntegerField(required=True)
    TABLE_SIZE_LIST = (
        ('two persons', 'TWO PERSONS'),
        ('four persons', 'FOUR PERSONS'),
        ('six persons', 'SIX PERSONS'),
        ('eight persons', 'EIGHT PERSONS'),
    )
    table_size = forms.ChoiceField(choices=TABLE_SIZE_LIST, required=True)
    date = forms.DateField(required=True, input_formats=['%Y-%m-%d', ])
    time_start = forms.TimeField(required=True, input_formats=['%H:%M', ])
    time_end = forms.TimeField(required=True, input_formats=['%H:%M', ])
