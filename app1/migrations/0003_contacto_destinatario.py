# Generated by Django 3.1.2 on 2020-10-18 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_contacto'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='destinatario',
            field=models.EmailField(default='nulle@nulle.com', max_length=254),
        ),
    ]
