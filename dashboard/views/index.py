from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView


class DashboardView(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        if user.is_staff or user.is_superuser or user.role == 'admin':
            return True
        return False

class DashboardTemplateView(DashboardView, TemplateView):
    template_name = 'dashboard/index.html'
