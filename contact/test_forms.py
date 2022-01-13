from django.test import TestCase
from contact.forms import ContactForm


class TestForms(TestCase):

    def test_contact_form_with_valid_data(self):
        form = ContactForm(data={
            'first_name': 'John',
            'last_name': 'Doe',
            'email_address': 'email@email.com',
            'message': 'test1'
        })

        self.assertTrue(form.is_valid())

    def test_contact_form_with_no_data(self):
        form = ContactForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 4)
