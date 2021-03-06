# Generated by Django 3.0.3 on 2020-04-11 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Challenges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=254)),
                ('score_max', models.IntegerField()),
                ('duree', models.IntegerField()),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainApp.Categories')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('prenom', models.CharField(max_length=200)),
                ('mail', models.EmailField(max_length=200)),
                ('addresse', models.CharField(max_length=200)),
                ('ville', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('mdp', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_score', models.DateTimeField()),
                ('score', models.IntegerField()),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainApp.Categories')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.Users')),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intitule', models.CharField(max_length=254)),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainApp.Categories')),
                ('challenge', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainApp.Challenges')),
            ],
        ),
        migrations.CreateModel(
            name='Accepted_Challenges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_defi_releve', models.DateTimeField()),
                ('date_debut_prevu', models.DateTimeField()),
                ('date_fin_effective', models.DateTimeField(default=None, null=True)),
                ('fini', models.BooleanField()),
                ('nb_essai', models.IntegerField(default=1)),
                ('pourcentage_completion', models.FloatField(default=0)),
                ('defi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.Challenges')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.Users')),
            ],
        ),
        migrations.AddConstraint(
            model_name='accepted_challenges',
            constraint=models.UniqueConstraint(fields=('user', 'defi', 'date_defi_releve'), name='unique_defi_releve'),
        ),
        migrations.AddConstraint(
            model_name='accepted_challenges',
            constraint=models.CheckConstraint(check=models.Q(pourcentage_completion__gte=0), name='check_pourcentage_gte_1'),
        ),
        migrations.AddConstraint(
            model_name='accepted_challenges',
            constraint=models.CheckConstraint(check=models.Q(pourcentage_completion__lte=1), name='check_pourcentage_lte_1'),
        ),
    ]
