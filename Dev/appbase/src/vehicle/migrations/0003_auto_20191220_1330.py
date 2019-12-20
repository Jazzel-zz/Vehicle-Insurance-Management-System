# Generated by Django 2.2.5 on 2019-12-20 13:30

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vehicle', '0002_auto_20191220_1329'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='VehicleModel',
            new_name='Vehicle',
        ),
        migrations.RenameField(
            model_name='vehicle',
            old_name='owner_name',
            new_name='name',
        ),
    ]
