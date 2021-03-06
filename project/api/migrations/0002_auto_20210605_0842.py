# Generated by Django 3.2.4 on 2021-06-05 08:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cms',
            name='phone',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{10,10}$')]),
        ),
        migrations.AlterField(
            model_name='cms',
            name='pincode',
            field=models.CharField(max_length=6, validators=[django.core.validators.RegexValidator('^\\d{1,6}$')]),
        ),
    ]
