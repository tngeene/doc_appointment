# Generated by Django 3.1.3 on 2020-12-30 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20201230_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='users.department'),
        ),
    ]
