# Generated by Django 4.2.5 on 2023-10-20 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0033_alter_order_options_order_stripe_cancel_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='foreignorder',
            name='stripe_cancel_id',
            field=models.CharField(blank=True, max_length=350, null=True, verbose_name='Stripe cancel ID'),
        ),
    ]