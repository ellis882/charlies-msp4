from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .forms import ContactForm


def send_email(request):
    """
    when user send email to restaurant and all
    required fields are fiiled in message goes
    to admin@example.com at backend and user
    gets a respond succes message
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

        try:
            send_mail(subject, message, 'admin@example.com',
                      ['admin@example.com'])

        except BadHeaderError:
            return HttpResponse('invalid header found.')

        return redirect('contact:send_success')

    else:
        form = ContactForm()

    context = {
        'form': form
        }

    return render(request, 'contact/contact.html', context)


def send_success(request):
    return HttpResponse('Thanks for your email we will contact you soon!')
