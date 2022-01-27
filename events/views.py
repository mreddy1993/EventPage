from ast import Pass
from django.shortcuts import render
from django.views.generic import ListView

from .models import eventModels

# Create your views here.


class eventsView(ListView):
    models = eventModels
    template_name = "calendar.html"