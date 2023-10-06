# Generated by Django 4.2.5 on 2023-10-05 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0015_alter_paypalproduct_product_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='StripeProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name of the product')),
                ('description', models.TextField(max_length=3000, verbose_name='Description')),
                ('product_id', models.CharField(blank=True, max_length=300, null=True, verbose_name='Stripe product ID')),
                ('price_id', models.CharField(blank=True, max_length=350, null=True, verbose_name='Stripe product price ID')),
            ],
            options={
                'verbose_name': 'stripe product',
                'verbose_name_plural': 'Stripe products',
                'db_table': 'stripe_products',
            },
        ),
    ]
