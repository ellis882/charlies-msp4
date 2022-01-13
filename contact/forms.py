from django import forms


class ContactForm(forms.Form):
    """
    required info for contact form to send
    message to restaurant
    """
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email_address = forms.EmailField(max_length=150, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True,
                              max_length=1000)
