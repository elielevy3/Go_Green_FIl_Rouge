# Generated by Django 3.0.4 on 2020-04-13 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_auto_20200413_0756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='challenge',
        ),
    ]