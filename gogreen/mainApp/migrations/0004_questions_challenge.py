# Generated by Django 3.0.4 on 2020-04-13 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_remove_questions_challenge'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='challenge',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='mainApp.Challenges'),
            preserve_default=False,
        ),
    ]
