from django.urls import path

from ..views.departments import (DepartmentCreateView, DepartmentDeleteView,
                                 DepartmentDetailView, DepartmentListView,
                                 DepartmentUpdateView)

app_name = "departments"

urlpatterns = [
    path('all/', DepartmentListView.as_view(), name="departments_list"),
    path('add/', DepartmentCreateView.as_view(), name="department_add"),
    path('<int:pk>/edit', DepartmentUpdateView.as_view(), name="department_update"),
    path('<int:pk>/details', DepartmentDetailView.as_view(), name="department_details"),
    path('<int:pk>/delete', DepartmentDeleteView.as_view(), name="department_delete"),
]
