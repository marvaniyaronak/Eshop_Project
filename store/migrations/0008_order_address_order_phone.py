# Generated by Django 4.1.4 on 2023-01-19 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, default='', max_length=60),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
    ]
