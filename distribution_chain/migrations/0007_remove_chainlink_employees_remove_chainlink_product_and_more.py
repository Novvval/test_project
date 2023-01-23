# Generated by Django 4.1.5 on 2023-01-23 06:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('distribution_chain', '0006_alter_product_release_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chainlink',
            name='employees',
        ),
        migrations.RemoveField(
            model_name='chainlink',
            name='product',
        ),
        migrations.AddField(
            model_name='chainlink',
            name='employees',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL, verbose_name='Сотрудники'),
        ),
        migrations.AddField(
            model_name='chainlink',
            name='product',
            field=models.ManyToManyField(blank=True, null=True, to='distribution_chain.product', verbose_name='Продукт'),
        ),
    ]
