# Generated by Django 4.2.4 on 2023-11-06 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_alter_movie_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='movie',
            name='synopsis',
            field=models.TextField(blank=True, default=''),
        ),
    ]
