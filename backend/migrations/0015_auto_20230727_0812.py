# Generated by Django 3.2 on 2023-07-27 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0014_room_occupants'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={},
        ),
        migrations.AlterModelManagers(
            name='student',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='student',
            name='email',
        ),
        migrations.RemoveField(
            model_name='student',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='last_name',
        ),
        migrations.AlterField(
            model_name='student',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='username',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
