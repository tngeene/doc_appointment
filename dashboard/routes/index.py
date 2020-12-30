from django.urls import path

from ..views.index import DashboardTemplateView, UserConfirmSuspendView
from ..views.admin_actions import activate_user, suspend_user

app_name = "index"

urlpatterns = [
    path('', DashboardTemplateView.as_view(),name="index"),
    path('users/<int:pk>/confirm-deactivation',
         UserConfirmSuspendView.as_view(), name="user_confirm_suspension"),
    path('users/<int:pk>/suspend_user', suspend_user, name="user_suspend_action"),
    path('users/<int:pk>/unsuspend_user',
         activate_user, name="user_unsuspend_action"),
]