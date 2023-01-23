# Generated by Django 4.1.5 on 2023-01-23 05:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('distribution_chain', '0004_alter_chainlink_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='address',
        ),
        migrations.RemoveField(
            model_name='chainlink',
            name='contact',
        ),
        migrations.AddField(
            model_name='chainlink',
            name='city',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Город'),
        ),
        migrations.AddField(
            model_name='chainlink',
            name='country',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Страна'),
        ),
        migrations.AddField(
            model_name='chainlink',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Электронная почта'),
        ),
        migrations.AddField(
            model_name='chainlink',
            name='street',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Улица'),
        ),
        migrations.AddField(
            model_name='chainlink',
            name='street_number',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Номер дома'),
        ),
        migrations.RemoveField(
            model_name='chainlink',
            name='employees',
        ),
        migrations.RemoveField(
            model_name='chainlink',
            name='product',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.AddField(
            model_name='chainlink',
            name='employees',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Сотрудники'),
        ),
        migrations.AddField(
            model_name='chainlink',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='distribution_chain.product', verbose_name='Продукт'),
        ),
    ]
