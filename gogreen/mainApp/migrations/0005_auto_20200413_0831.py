# Generated by Django 3.0.4 on 2020-04-13 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0004_questions_challenge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='mdp',
            field=models.CharField(max_length=50),
        ),
        migrations.AddConstraint(
            model_name='users',
            constraint=models.UniqueConstraint(fields=('mail',), name='unique_user_mail'),
        ),
    ]
