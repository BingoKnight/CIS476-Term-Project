# Generated by Django 2.2.7 on 2019-11-27 00:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0002_auto_20191126_1937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flightmodel',
            name='trip_type',
        ),
    ]
