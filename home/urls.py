from django.urls import path

from .views import HomePageTemplateView

app_name = 'home'

urlpatterns = [
    path('',HomePageTemplateView.as_view(), name='homepage')
]
