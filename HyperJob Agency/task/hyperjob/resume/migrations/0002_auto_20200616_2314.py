# Generated by Django 2.2 on 2020-06-16 23:14

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Vacancy',
            new_name='Resume',
        ),
    ]