from django.shortcuts import render


def index(request):
    """
    restaurant app is home page of website with index.html
    """
    context = {}
    print(True)
    return render(request, "restaurant/index.html", context)
