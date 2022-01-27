from importlib.resources import path
from django.urls import URLPattern, include, path
from .views import eventsView

urlpatterns = [
    path("events/", eventsView.as_view(), name = "events")


]