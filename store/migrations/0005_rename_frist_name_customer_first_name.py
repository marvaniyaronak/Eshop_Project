# Generated by Django 4.1.4 on 2023-01-04 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_customer_alter_product_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='frist_name',
            new_name='first_name',
        ),
    ]
