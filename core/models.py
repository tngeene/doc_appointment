from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class CommonInfo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

User = get_user_model()
class Event(CommonInfo):
    name = models.CharField(max_length=254)
    description = models.TextField()
    photo  = models.ImageField(upload_to="events/photos", null=True, blank=True)
    date = models.DateTimeField()
    attendees = models.ManyToManyField(User, related_name='events_attending', blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events_added')


class Service(CommonInfo):
    name = models.CharField(max_length=254)
    description = models.TextField()

class Appointment(CommonInfo):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'doctor'}, related_name='appointments_requested', blank=True)
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments_made')
    date = models.DateTimeField()
    is_confirmed = models.BooleanField(default=False)
    confirmed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments_confirmed', blank=True, null=True)



