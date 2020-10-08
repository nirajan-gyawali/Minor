# Generated by Django 3.1.1 on 2020-10-07 17:26

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0011_auto_20201007_1721'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='doctors',
            new_name='doctor',
        ),
        migrations.RenameModel(
            old_name='hospitals',
            new_name='hospital',
        ),
        migrations.RenameModel(
            old_name='notification_for_doctors',
            new_name='notification_for_doctor',
        ),
        migrations.RenameModel(
            old_name='notification_for_patients',
            new_name='notification_for_patient',
        ),
    ]
