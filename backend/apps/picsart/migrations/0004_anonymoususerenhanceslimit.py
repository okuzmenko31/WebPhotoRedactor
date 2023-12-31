# Generated by Django 4.2.5 on 2023-10-08 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picsart', '0003_anonymoususerfunctionsusagecounter_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnonymousUserEnhancesLimit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('limit', models.IntegerField(default=5, verbose_name='Limit for all feature for unauthorized users')),
            ],
            options={
                'verbose_name': 'limit',
                'verbose_name_plural': 'Limits for anonymous users',
                'db_table': 'anonymous_user_enhances_limit',
            },
        ),
    ]
