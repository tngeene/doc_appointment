from django.urls import path

from .views import DepartmentListAPIView, DoctorListAPIView

app_name='users'

urlpatterns = [
    path('doctors/',DoctorListAPIView.as_view(),name='departmental_doctors'),
    path('departments/',DepartmentListAPIView.as_view(),name='departments'),
]
