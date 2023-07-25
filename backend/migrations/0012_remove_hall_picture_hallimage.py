# Generated by Django 4.2.3 on 2023-07-25 04:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0011_alter_message_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hall',
            name='picture',
        ),
        migrations.CreateModel(
            name='HallImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='hall/')),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.hall')),
            ],
        ),
    ]
