# Generated by Django 4.2.5 on 2023-10-20 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0032_alter_order_created_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-created_at'], 'verbose_name': 'order', 'verbose_name_plural': 'Orders'},
        ),
        migrations.AddField(
            model_name='order',
            name='stripe_cancel_id',
            field=models.CharField(blank=True, max_length=350, null=True, verbose_name='Stripe cancel ID'),
        ),
    ]