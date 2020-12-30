from django.urls import path, include

app_name = "dashboard"

urlpatterns = [
    path('', include('dashboard.routes.index')),
    path('doctors/', include('dashboard.routes.doctors')),
    path('patients/', include('dashboard.routes.patients')),
    path('events/', include('dashboard.routes.events')),
]


