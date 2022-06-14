from importlib.resources import path
from django.urls import include, path
from .views import aboutView, eventDetails, eventsView, eventCreate, eventUpdate, eventDelete

urlpatterns = [
    path("", eventsView.as_view(), name = "events"),
    path("about/", aboutView.as_view(), name = "about"),
    path("new/", eventCreate.as_view(), name = "create"),
    path("<int:pk>/", eventDetails.as_view(), name = "detail"),
    path("<int:pk>/edit", eventUpdate.as_view(), name = "update"),
    path("<int:pk>/delete", eventDelete.as_view(), name = "delete"),
]