# Generated by Django 2.0.4 on 2018-04-13 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_game_gameend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='timer',
            field=models.IntegerField(default=20),
        ),
    ]
