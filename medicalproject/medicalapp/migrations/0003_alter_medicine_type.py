# Generated by Django 3.2.13 on 2022-04-27 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicalapp', '0002_medicine_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='type',
            field=models.CharField(max_length=250),
        ),
    ]