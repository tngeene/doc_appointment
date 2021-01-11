from django.views.generic import  ListView, DeleteView
from django.contrib import messages
from django.views.generic.detail import DetailView
from core.models import Event
from .index import DashboardView
from django.urls import reverse_lazy

class EventListView(DashboardView, ListView):
    model = Event
    template_name = 'doctor-dashboard/events/list.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context["events"] = user.events_attending.all().order_by("-pk")
        return context


class EventDetailView(DashboardView, DetailView):
    model = Event
    context_object_name = 'event'
    template_name = 'doctor-dashboard/events/details.html'

