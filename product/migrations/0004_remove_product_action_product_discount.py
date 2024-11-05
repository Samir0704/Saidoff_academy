# Generated by Django 5.1 on 2024-08-27 06:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_remove_product_discount_product_discount_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='action',
        ),
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.action'),
        ),
    ]
