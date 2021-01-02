from django.urls import path

from .views import HomePageTemplateView, UserProfilePage

app_name = 'home'

urlpatterns = [
    path('',HomePageTemplateView.as_view(), name='homepage'),
    path('profile/',UserProfilePage.as_view(), name='my_profile'),
]
