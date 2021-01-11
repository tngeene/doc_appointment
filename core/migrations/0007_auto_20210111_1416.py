# Generated by Django 3.1.3 on 2021-01-11 11:16

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0006_event_venue'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='appointment',
            unique_together={('doctor', 'date')},
        ),
    ]
