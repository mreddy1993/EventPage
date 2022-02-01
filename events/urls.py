from importlib.resources import path
from django.urls import include, path
from .views import eventsView

urlpatterns = [
    path("events/", eventsView.as_view(), name = "events")


]