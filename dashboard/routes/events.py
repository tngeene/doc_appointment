from django.urls import path

from ..views.events import (EventCreateView, EventDetailView, EventListView,
                            EventUpdateView)

app_name = "events"

urlpatterns = [
    path('all/', EventListView.as_view(), name='events_list'),
    path('add/', EventCreateView.as_view(), name='event_add'),
    path('<int:pk>/details/', EventDetailView.as_view(), name='event_details'),
    path('<int:pk>/edit/', EventUpdateView.as_view(), name='event_update'),
]
