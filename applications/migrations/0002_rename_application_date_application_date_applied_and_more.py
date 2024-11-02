# Generated by Django 5.1.2 on 2024-10-24 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='application_date',
            new_name='date_applied',
        ),
        migrations.AddField(
            model_name='application',
            name='status',
            field=models.CharField(default='pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='application',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
