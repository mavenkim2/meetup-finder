# Generated by Django 3.1.1 on 2020-11-24 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='xcoord',
        ),
        migrations.RemoveField(
            model_name='event',
            name='ycoord',
        ),
        migrations.AddField(
            model_name='event',
            name='address',
            field=models.CharField(default='Address', max_length=500, verbose_name='Address'),
        ),
    ]
