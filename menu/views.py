from django.shortcuts import render
from .models import Menu, Category, Specials


def meals_list(request):
    """
    get each meal in the menu with description and price
    in different category that can be managed at the
    list.html page
    """
    meals_list = Menu.objects.all()
    categories = Category.objects.all()
    specials = Specials.objects.all()

    context = {
        'meals_list': meals_list,
        'categories': categories,
        'specials': specials
    }

    return render(request, 'menu/list.html', context)
