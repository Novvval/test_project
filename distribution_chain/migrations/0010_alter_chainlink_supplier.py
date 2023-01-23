# Generated by Django 4.1.5 on 2023-01-23 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('distribution_chain', '0009_alter_chainlink_employees_alter_chainlink_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chainlink',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='distribution_chain.chainlink', verbose_name='Поставщик'),
        ),
    ]
