from django.views.generic import TemplateView
from django.contrib.auth import get_user_model
from users.models import Department

User = get_user_model()
# Create your views here.

# index view
class HomePageTemplateView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        doctors = User.objects.filter(role='doctor')
        doctors_count = doctors.count()
        doctors = doctors[0:5]
        context['departments']=Department.objects.all()
        context['doctors']=doctors
        context['doctors_count']=doctors_count
        return context

