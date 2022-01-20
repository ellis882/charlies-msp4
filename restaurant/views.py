from django.shortcuts import render
from .models import Media


def index(request):
    """
    restaurant app is home page of website with index.html
    """
    pictures = Media.objects.all()
    context = {'pictures': pictures }
    print(True)
    return render(request, "restaurant/index.html", context)
