from ast import Pass
from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView

from .models import eventModels

# Create your views here.


class eventsView(ListView):
    model = eventModels
    template_name = "home.html"

class aboutView(TemplateView):
    template_name = "about.html"

class eventCreate(CreateView):
    model = eventModels
    template_name = "event_create.html"
    fields = ["title", "date","eventDescription", "location"]

class eventDetails(DetailView):
    model = eventModels
    template_name = "event_detail.html"

class eventUpdate(UpdateView):
    model = eventModels
    template_name = "event_update"