from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Flat(models.Model):
#    owner = models.CharField('ФИО владельца', max_length=200)
    created_at = models.DateTimeField(
        'Когда создано объявление',
        default=timezone.now,
        db_index=True)

    description = models.TextField('Текст объявления', blank=True)
    price = models.IntegerField('Цена квартиры', db_index=True)

    town = models.CharField(
        'Город',
        max_length=50,
        db_index=True)
    town_district = models.CharField(
        'Район',
        max_length=50,
        blank=True,
        help_text='Чертаново Южное')
    address = models.TextField(
        'Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4')
    floor = models.CharField(
        'Этаж',
        max_length=3,
        help_text='Первый этаж, последний этаж, пятый этаж')

    rooms_number = models.IntegerField(
        'Количество комнат',
        db_index=True)
    living_area = models.IntegerField(
        'Жилая площадь кв.м.',
        null=True,
        blank=True,
        db_index=True)

    has_balcony = models.NullBooleanField('Наличие балкона', db_index=True)
    active = models.BooleanField('Активное объявление', db_index=True)
    construction_year = models.IntegerField(
        'Год постройки',
        null=True,
        blank=True,
        db_index=True)
    new_building = models.BooleanField('Новостройка', blank=True, null=True)

    liked_by = models.ManyToManyField(
        User,
        verbose_name="Кто лайкнул",
        related_name="liked_flats",
        blank=True
    )

    # owner_pure_phone = PhoneNumberField(
    #     'Нормализованный номер владельца',
    #     blank=True,
    #     null=True
    # )

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'


class Complaint(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Кто жаловался",
        related_name="complaints"
    )
    flat = models.ForeignKey(
        Flat,
        on_delete=models.CASCADE,
        verbose_name="Квартира, на которую пожаловались",
        related_name="complaints"
    )
    text = models.TextField(verbose_name="Текст жалобы", blank=True)

    def __str__(self):
        return f'Жалоба на {self.flat} от {self.user}'


class Owner(models.Model):
    name = models.CharField('ФИО владельца', max_length=200)
    pure_phone = PhoneNumberField(
        'Нормализованный номер владельца',
        blank=True,
        null=True
    )
    owned_flats = models.ManyToManyField(
        Flat,
        verbose_name='Имеющиеся квартиры',
        related_name="owners"
    )

    def __str__(self):
        return self.name