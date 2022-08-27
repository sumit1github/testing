# Generated by Django 4.0.6 on 2022-07-29 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('contact1', models.CharField(blank=True, max_length=255, null=True)),
                ('contact2', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('date_of_joining', models.DateField(blank=True, null=True)),
                ('date_of_leaving', models.DateField(blank=True, null=True)),
                ('addhar_number', models.CharField(blank=True, max_length=255, null=True)),
                ('driving_lisence', models.CharField(blank=True, max_length=255, null=True)),
                ('pan_card', models.CharField(blank=True, max_length=255, null=True)),
                ('bank_ac_number', models.CharField(blank=True, max_length=255, null=True)),
                ('ifsc_code', models.CharField(blank=True, max_length=255, null=True)),
                ('basic_salary', models.FloatField(default=0.0)),
                ('extra_money', models.FloatField(default=0.0)),
                ('advance', models.FloatField(default=0.0)),
                ('is_active', models.BooleanField(default=True)),
                ('extra_info', models.TextField(blank=True, null=True)),
            ],
        ),
    ]