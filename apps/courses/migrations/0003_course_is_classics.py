# Generated by Django 2.2 on 2022-05-16 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_course_org'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='is_classics',
            field=models.BooleanField(default=False, verbose_name='是否经典'),
        ),
    ]
