# Generated by Django 3.0.4 on 2020-04-19 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0006_auto_20200419_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accepted_challenges',
            name='fini',
            field=models.BooleanField(default=False),
        ),
    ]
