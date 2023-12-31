# Generated by Django 4.2.5 on 2023-10-15 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0026_remove_plan_paypal_plan_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='foreignorder',
            name='paypal_order_id',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='PayPal order id'),
        ),
        migrations.AddField(
            model_name='foreignorder',
            name='stripe_session_id',
            field=models.CharField(blank=True, max_length=350, null=True, verbose_name='Stripe session id'),
        ),
    ]
