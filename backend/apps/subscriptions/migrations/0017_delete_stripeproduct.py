# Generated by Django 4.2.5 on 2023-10-05 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0016_stripeproduct'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StripeProduct',
        ),
    ]
