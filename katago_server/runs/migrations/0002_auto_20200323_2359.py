# Generated by Django 3.0.1 on 2020-03-23 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='run',
            name='data_board_len',
            field=models.IntegerField(default=19, verbose_name='data board len'),
        ),
        migrations.AddField(
            model_name='run',
            name='inputs_version',
            field=models.IntegerField(default=7, verbose_name='inputs version for model features'),
        ),
        migrations.AddField(
            model_name='run',
            name='max_search_threads_allowed',
            field=models.IntegerField(default=8, verbose_name='max search threads server promises to never exceed'),
        ),
    ]
