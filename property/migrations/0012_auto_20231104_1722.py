# Generated by Django 2.2.24 on 2023-11-04 14:22

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_auto_20231104_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='active',
            field=models.BooleanField(db_index=True, verbose_name='Активное объявление'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='construction_year',
            field=models.IntegerField(blank=True, db_index=True, null=True, verbose_name='Год постройки'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='living_area',
            field=models.IntegerField(blank=True, db_index=True, null=True, verbose_name='Жилая площадь кв.м.'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='rooms_number',
            field=models.IntegerField(db_index=True, verbose_name='Количество комнат'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='town',
            field=models.CharField(db_index=True, max_length=50, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='town_district',
            field=models.CharField(blank=True, help_text='Чертаново Южное', max_length=50, verbose_name='Район'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='pure_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Нормализованный номер владельца'),
        ),
    ]
