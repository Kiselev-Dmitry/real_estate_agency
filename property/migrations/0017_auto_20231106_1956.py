# Generated by Django 2.2.24 on 2023-11-06 16:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0015_remove_flat_owners_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_complains', to=settings.AUTH_USER_MODEL, verbose_name='Кто жаловался'),
        ),
    ]
