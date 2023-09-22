# Generated by Django 4.2.5 on 2023-09-19 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FootballGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lower_score', models.IntegerField()),
                ('higher_score', models.IntegerField()),
                ('date', models.DateField()),
                ('loser', models.CharField(max_length=100)),
                ('winner', models.CharField(max_length=100)),
            ],
        ),
    ]
