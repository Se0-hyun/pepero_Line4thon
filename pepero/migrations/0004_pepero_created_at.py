# Generated by Django 4.2.4 on 2023-11-10 16:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pepero', '0003_pepero_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='pepero',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
