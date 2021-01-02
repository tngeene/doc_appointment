from django.urls import path, include

app_name = "doctor_dashboard"

urlpatterns = [
    path('', include('doctor_dashboard.routes.index')),
    path('appointments/', include('doctor_dashboard.routes.appointments')),
    # path('doctors/', include('doctor_dashboard.routes.doctors')),
    # path('patients/', include('doctor_dashboard.routes.patients')),
    path('events/', include('doctor_dashboard.routes.events')),
]


