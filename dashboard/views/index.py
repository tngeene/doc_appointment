from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView, DetailView
from django.contrib.auth import get_user_model

User = get_user_model()

class DashboardView(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        if user.is_staff or user.is_superuser or user.role == 'admin':
            return True
        return False

class DashboardTemplateView(DashboardView, TemplateView):
    template_name = 'dashboard/index.html'

    def get_context_data(self, **kwargs):
        doctors = User.objects.filter(role='doctor')
        context = super().get_context_data(**kwargs)
        context["doctors_count"] = doctors.count()
        context["recent_doctors"] = doctors.order_by('-pk')[:10]
        return context


class UserConfirmSuspendView(DashboardView, DetailView):
    model = User
    context_object_name = 'user'
    template_name = 'dashboard/users/confirm-suspension.html'
