# Generated by Django 4.0.6 on 2022-08-06 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app3_employee_management', '0004_employeedocuments'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='designation',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='locker_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='working_hour',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
