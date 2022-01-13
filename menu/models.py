from django.db import models
from django.utils.text import slugify


class Menu(models.Model):
    """
    menu card of restaurant can be managed from admin panel
    all important info is available to manage
    """
    objects = models.Manager()
    meal = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL,
                                 null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.meal:
            self.slug = slugify(self.meal)
        super(Menu, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'menu'
        verbose_name_plural = 'menu'

    def __str__(self):
        return str(self.meal)


class Category(models.Model):
    """
    the category steaks, desserts and specials
    that is showed at the frontend
    """
    objects = models.Manager()
    title = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return str(self.title)
