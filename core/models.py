from django.db import models
from django.contrib.auth import get_user_model
from users.models import Department
# Create your models here.
class CommonInfo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

User = get_user_model()
class Event(CommonInfo):
    name = models.CharField(max_length=254)
    venue = models.CharField(max_length=254, null=True)
    description = models.TextField()
    photo  = models.ImageField(upload_to="events/photos", null=True, blank=True)
    date = models.DateTimeField()
    attendees = models.ManyToManyField(User, related_name='events_attending', blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events_added')

    def __str__(self) -> str:
        return self.name


STATUS_CHOICES = [
    ('confirmed', 'confirmed'),
    ('pending', 'pending'),
    ('declined', 'declined'),
]

class Appointment(CommonInfo):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='appointments', null=True, blank=True)
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'doctor'}, related_name='appointments_requested', blank=True, null=True)
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments_made', null=True, blank=True)
    date = models.DateTimeField()
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    message = models.TextField(default='-')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='pending')
    confirmed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments_confirmed', blank=True, null=True)

    def __str__(self) -> str:
        return f'Appointment by {self.name} on {self.date}'





