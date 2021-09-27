# Generated by Django 3.2.7 on 2021-09-13 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Succession_Cast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField()),
                ('birthday', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Succession_Season_Episodes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField()),
                ('episodeAirDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Succession_Seasons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField()),
                ('seasonNum', models.IntegerField()),
                ('imdbUrl', models.URLField()),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='django_world.succession_season_episodes')),
            ],
        ),
        migrations.CreateModel(
            name='Succession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('cast', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='django_world.succession_cast')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='django_world.succession_seasons')),
            ],
        ),
    ]