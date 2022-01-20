from django.db import models


class Media (models.Model):
    section_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='index/')

    class Meta:
        verbose_name = 'media'
        verbose_name_plural = 'media'

    def __str__(self):
        return str(self.section_name)
