# Generated by Django 4.1.5 on 2023-01-23 06:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('distribution_chain', '0008_rename_product_chainlink_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chainlink',
            name='employees',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Сотрудники'),
        ),
        migrations.AlterField(
            model_name='chainlink',
            name='products',
            field=models.ManyToManyField(blank=True, to='distribution_chain.product', verbose_name='Продукт'),
        ),
    ]
