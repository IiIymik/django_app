# Generated by Django 4.0 on 2021-12-27 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('balance', '0005_remove_transaction_credit_remove_transaction_debet_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
