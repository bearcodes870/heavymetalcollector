# Generated by Django 3.1 on 2020-12-19 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_albumtype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='albumtype',
            name='owned',
        ),
        migrations.AlterField(
            model_name='albumtype',
            name='albumtype',
            field=models.CharField(choices=[('V', 'Vinyl'), ('C', 'CD'), ('D', 'Digital'), ('T', 'Tape')], default='V', max_length=1),
        ),
        migrations.AlterField(
            model_name='albumtype',
            name='date_acquired',
            field=models.DateField(verbose_name='date acquired'),
        ),
    ]
