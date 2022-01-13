from django.test import TestCase
from .views import send_email
from .forms import ContactForm


class TestContactForm(TestCase):

    def test_can_send_message(self):
        data = {
            'first_name': 'Jonh',
            'last_name': 'Doe',
            'email_address': 'email1@email.com',
            'message': 'would love to talk about food',

        }
        response = self.client.post('contact/contact.html', data=data)
        self.assertTemplateUsed(response, 'contact/contact.html')
        self.assertContains(response, 'first_name')
        self.assertContains(response, 'last_name')
        self.assertContains(response, 'email_address')
        self.assertEqual(ContactForm.objects.count(), 1)
        self.assertRedirects(response, 'contact:send_success')
