from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from users.views import  logout_user, login_redirect, LoginUserView, SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('core/', include('core.urls')),
    path('users/', include('users.urls')),
    path('accounts/', include('allauth.urls')),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('accounts/logout', logout_user, name='logout'),
    path('accounts/login/', LoginUserView.as_view(), name='account_login'),
    path('accounts/login-redirect/', login_redirect, name='login_redirect'),

    path('admin-dashboard/', include('dashboard.urls', namespace='dashboard')),
    path('dashboard/', include('doctor_dashboard.urls', namespace='doctor_dashboard')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
