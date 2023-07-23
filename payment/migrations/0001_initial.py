# Generated by Django 4.2.3 on 2023-07-21 00:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('backend', '0003_booking_paid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_price_id', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.room')),
            ],
        ),
    ]