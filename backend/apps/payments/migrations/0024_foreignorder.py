# Generated by Django 4.2.5 on 2023-10-15 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0023_order_stripe_session_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForeignOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ext_id', models.CharField(max_length=250, verbose_name='Internal order ID')),
                ('amount', models.IntegerField(verbose_name='Amount')),
                ('currency', models.CharField(max_length=50, verbose_name='Currency')),
                ('email', models.EmailField(blank=True, max_length=350, null=True, verbose_name='Email')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('success_url', models.URLField(blank=True, null=True, verbose_name='Return success url')),
                ('cancel_url', models.URLField(blank=True, null=True, verbose_name='Return cancel url')),
                ('notify_url', models.URLField(blank=True, null=True, verbose_name='Notify url')),
            ],
            options={
                'verbose_name': 'foreign order',
                'verbose_name_plural': 'Foreign Orders',
                'db_table': 'foreign_orders',
            },
        ),
    ]
