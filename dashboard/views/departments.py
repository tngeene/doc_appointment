from django.contrib import auth, messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from django.views.generic.list import ListView
from users.models import Department

from ..views.index import DashboardView

User = auth.get_user_model()


class DepartmentCreateView(DashboardView, CreateView):
    model = Department
    fields = ('name', 'description', 'cover_photo',)
    template_name = 'dashboard/departments/add.html'

    def get_success_url(self) -> str:
        messages.success(self.request, "Department Added Successfully")
        return reverse_lazy('dashboard:departments:department_details', kwargs={'pk': self.object.pk})


class DepartmentUpdateView(DashboardView, UpdateView):
    model = Department
    fields = ('name', 'description', 'cover_photo',)
    template_name = 'dashboard/departments/edit.html'

    def get_success_url(self) -> str:
        messages.success(self.request, "Department Updated Successfully")
        return reverse_lazy('dashboard:departments:department_details', kwargs={'pk': self.object.pk})


class DepartmentListView(DashboardView, ListView):
    model = Department
    context_object_name = 'departments'
    template_name = 'dashboard/departments/list.html'


class DepartmentDetailView(DashboardView, DetailView):
    model = Department
    context_object_name = 'department'
    template_name = 'dashboard/departments/details.html'

    def get_context_data(self, **kwargs):
        department = self.object.id
        context = super().get_context_data(**kwargs)
        context["doctors"] = User.objects.filter(department=department, role="doctor")
        context["users"] = User.objects.filter(department=department, role="staff")
        return context


class DepartmentDeleteView(DashboardView, DeleteView):
    model = Department
    template_name = 'dashboard/departments/confirm-delete.html'
    context_object_name = 'department'

    def get_success_url(self) -> str:
        messages.success(self.request, "Department Deleted Successfully.")
        return reverse_lazy('dashboard:departments:departments_list')
