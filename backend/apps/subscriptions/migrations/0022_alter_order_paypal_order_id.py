# Generated by Django 4.2.5 on 2023-10-14 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0021_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='paypal_order_id',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='PayPal order id'),
        ),
    ]
