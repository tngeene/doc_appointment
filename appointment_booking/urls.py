from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('core/', include('core.urls')),
    path('users/', include('users.urls')),
    path('accounts/', include('allauth.urls')),
    path('admin-dashboard/', include('dashboard.urls', namespace='dashboard')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
