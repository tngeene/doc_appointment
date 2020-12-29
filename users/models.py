from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _
from core.models import CommonInfo

class UserAccountManager(UserManager):
    def create_user(self, username=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, email, password, **extra_fields)

    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff status.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Super user must have is_superuser status')

        return self._create_user(email, email, password, **extra_fields)

GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )


ROLE_CHOICES = (
    ('admin', 'admin'),
    ('doctor', 'doctor'),
    ('staff', 'staff'),
    ('patient', 'patient'),
)

class Specialization(CommonInfo):
    name = models.CharField(max_length=254)

class UserAccount(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='users/profile-photos/', null=True)
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    role = models.CharField(max_length=30,choices=ROLE_CHOICES,default='admin')
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='male')
    date_of_birth = models.DateField(null=True, blank=True)
    staff_id = models.CharField(max_length=50, null=True, blank=True)
    id_no = models.PositiveIntegerField(null=True, blank=True)
    specializations = models.ManyToManyField(Specialization, related_name='doctors', blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name',]

    objects = UserAccountManager()

    def __str__(self):
        return f"{self.get_full_name()}"
