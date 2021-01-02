from django.urls import path

from ..views.events import EventDetailView, EventListView


app_name = "events"

urlpatterns = [
    path('all/', EventListView.as_view(), name="events_list"),
    path('<int:pk>/details', EventDetailView.as_view(), name="event_details"),
]