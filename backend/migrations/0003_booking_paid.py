# Generated by Django 4.2.3 on 2023-07-21 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_remove_booking_end_time_remove_booking_start_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]