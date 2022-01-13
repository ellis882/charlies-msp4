from django.shortcuts import render
from .models import Team


def team_list(request):
    """
    get name, title and image from Team in models
    to use info for the templates in team.html
    """
    team_list = Team.objects.all()

    context = {
        'team_list': team_list,
    }

    return render(request, 'chefs/team.html', context)
