# Generated by Django 3.1.2 on 2020-11-08 17:39

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_auto_20201106_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='hobbies',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), size=None),
        ),
    ]
