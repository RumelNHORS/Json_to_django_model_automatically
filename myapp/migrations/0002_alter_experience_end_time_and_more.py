# Generated by Django 4.2.2 on 2023-06-12 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='end_time',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='start_time',
            field=models.DateField(blank=True, null=True),
        ),
    ]
