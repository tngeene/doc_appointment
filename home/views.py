from django.views.generic import TemplateView
# Create your views here.

# index view
class HomePageTemplateView(TemplateView):
    template_name = 'main/index.html'
