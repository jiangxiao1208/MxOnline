# Generated by Django 2.2 on 2022-05-16 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userask',
            old_name='course',
            new_name='course_name',
        ),
    ]
