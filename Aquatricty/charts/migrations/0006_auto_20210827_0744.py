# Generated by Django 3.2.6 on 2021-08-27 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0005_auto_20210827_0743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emails',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='ip_address',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
