from django.shortcuts import render
from .models import Menu, Category


def meals_list(request):
    """
    get each meal in the menu with description and price
    in different category that can be managed at the
    list.html page
    """
    meals_list = Menu.objects.all()
    categories = Category.objects.all()

    context = {
        'meals_list': meals_list,
        'categories': categories,
    }

    return render(request, 'menu/list.html', context)
