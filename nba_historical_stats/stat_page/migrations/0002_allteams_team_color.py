# Generated by Django 4.1.7 on 2023-05-28 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stat_page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='allteams',
            name='team_color',
            field=models.CharField(default='', max_length=7),
        ),
    ]
