# Generated by Django 4.1.4 on 2023-01-19 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_rename_frist_name_customer_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]
