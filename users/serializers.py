from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

from .models import Department

User = get_user_model()


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name',)


class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'name',)
