# Generated by Django 3.1.1 on 2020-11-24 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20201124_0759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]