# Generated by Django 2.2.24 on 2023-11-07 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0021_auto_20231107_2122'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='owned_flats',
            new_name='flats',
        ),
    ]
