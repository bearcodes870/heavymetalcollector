# Generated by Django 3.1 on 2020-12-23 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20201223_0532'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='instruments',
            field=models.ManyToManyField(to='main_app.Instrument'),
        ),
    ]