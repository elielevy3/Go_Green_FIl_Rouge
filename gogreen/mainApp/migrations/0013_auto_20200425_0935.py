# Generated by Django 3.0.5 on 2020-04-25 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0012_remove_accepted_challenges_nb_essai'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenges',
            name='facile',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='challenges',
            name='ponctuel',
            field=models.BooleanField(default=False),
        ),
    ]
