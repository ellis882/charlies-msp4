from django.db import models


class Team(models.Model):
    """
    name and title of the leading team of the restaurant
    in the admin panel that can be managed from
    the backend side
    """
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='team/')

    class Meta:
        verbose_name = 'team'
        verbose_name_plural = 'team'

    def __str__(self):
        return str(self.name)
