# Generated by Django 2.2.4 on 2019-08-19 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ConfigurationApp', '0004_artist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='lastName',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
