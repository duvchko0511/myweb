# Generated by Django 5.0 on 2024-01-04 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0006_product_facebook_url_product_phone_url_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='phone_url',
        ),
        migrations.AddField(
            model_name='product',
            name='phone',
            field=models.TextField(blank=True, null=True),
        ),
    ]
