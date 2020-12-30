from django.urls import path

from .views import AppointMentCreateAPIView

app_name = 'core'

urlpatterns = [
    path('create-appointment/',AppointMentCreateAPIView.as_view(),name='create_appointment'),
]
