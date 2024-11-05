# Generated by Django 5.1 on 2024-08-28 18:37

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_user_telegram_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.AddField(
            model_name='user',
            name='company_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='company name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='full_name',
            field=models.CharField(max_length=255, verbose_name='full name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True, verbose_name='phone_number'),
        ),
        migrations.AlterField(
            model_name='user',
            name='telegram_id',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='telegram id'),
        ),
        migrations.AlterField(
            model_name='user',
            name='telegram_username',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='telegram username'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('legal', 'LEGAL'), ('individual', 'INDIVIDUAL')], default='individual', max_length=10, verbose_name='user type'),
        ),
    ]
