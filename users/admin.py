from django.contrib import admin
from .models import UserAccount, Specialization, Department
# Register your models here.
admin.site.register(UserAccount)
admin.site.register(Department)
admin.site.register(Specialization)