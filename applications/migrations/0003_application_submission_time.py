# Generated by Django 5.1.2 on 2024-10-28 15:54

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0002_rename_application_date_application_date_applied_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='submission_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]