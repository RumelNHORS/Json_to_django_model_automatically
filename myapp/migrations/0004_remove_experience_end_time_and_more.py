# Generated by Django 4.2.2 on 2023-06-12 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_experience_end_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experience',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='start_time',
        ),
    ]