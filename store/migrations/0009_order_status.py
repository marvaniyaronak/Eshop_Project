# Generated by Django 4.1.4 on 2023-01-20 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_order_address_order_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
