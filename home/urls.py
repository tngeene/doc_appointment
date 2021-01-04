from django.urls import path

from .views import (BookEventAttendanceAPIView, EventDetailPage,
                    HomePageTemplateView, UserProfilePage)

app_name = 'home'

urlpatterns = [
    path('',HomePageTemplateView.as_view(), name='homepage'),
    path('profile/',UserProfilePage.as_view(), name='my_profile'),
    path('events/<int:pk>/',EventDetailPage.as_view(), name='event'),
    path('events/booking/',BookEventAttendanceAPIView.as_view(), name='event_booking'),
]
