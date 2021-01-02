from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.contrib import messages
from django.views.generic.detail import DetailView
from core.models import Event
from .index import DashboardView
from django.urls import reverse_lazy

class EventCreateView(DashboardView, CreateView):
    model = Event
    fields = ('name', 'description', 'date', 'venue','photo')
    template_name = 'dashboard/events/add.html'

    def form_valid(self, form):
        user = self.request.user
        event = form.save(commit=False)
        event.created_by = user
        event.save()

        return super().form_valid(form)

    def get_success_url(self) -> str:
        messages.success(self.request, "Event Added Successfully")
        return reverse_lazy("dashboard:events:event_details", kwargs = {'pk': self.object.pk})


class EventListView(DashboardView, ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'dashboard/events/list.html'


class EventDetailView(DashboardView, DetailView):
    model = Event
    context_object_name = 'event'
    template_name = 'dashboard/events/details.html'


class EventUpdateView(DashboardView, UpdateView):
    model = Event
    fields = ('name', 'description', 'date', 'venue', 'photo')
    template_name = 'dashboard/events/edit.html'

    def form_valid(self, form):
        user = self.request.user
        event = form.save(commit=False)
        event.created_by = user
        event.save()

        return super().form_valid(form)

    def get_success_url(self) -> str:
        messages.success(self.request, "Event Updated Successfully")
        return reverse_lazy("dashboard:events:event_details", kwargs = {'pk': self.object.pk})