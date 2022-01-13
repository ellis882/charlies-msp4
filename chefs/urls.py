from django.urls import path
from . import views


app_name = 'chefs'

urlpatterns = [
    path('', views.team_list, name='team_list'),
]
