from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


from rest_framework.authentication import SessionAuthentication
class CSRFExemptMixin(SessionAuthentication):
    def enforce_csrf(self, request):
        return

# class CSRFExemptMixin(object):
#    @method_decorator(csrf_exempt)
#    def dispatch(self, *args, **kwargs):
#        return super().dispatch(*args, **kwargs)
