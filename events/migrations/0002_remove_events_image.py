# Generated by Django 3.2 on 2022-01-13 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='image',
        ),
    ]