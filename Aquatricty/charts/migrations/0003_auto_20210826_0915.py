# Generated by Django 3.2.6 on 2021-08-26 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0002_ip_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='ip_address',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='socialmedia',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
