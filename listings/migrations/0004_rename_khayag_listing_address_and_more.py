# Generated by Django 5.0 on 2023-12-20 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_listing_delete_teammember'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='khayag',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='listing',
            old_name='broom',
            new_name='bathrooms',
        ),
        migrations.RenameField(
            model_name='listing',
            old_name='aroom',
            new_name='bedrooms',
        ),
        migrations.RenameField(
            model_name='listing',
            old_name='duureg',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='listing',
            old_name='tailbar',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='listing',
            old_name='eronhii_zurag',
            new_name='photo_main',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='khoroo',
        ),
        migrations.AddField(
            model_name='listing',
            name='state',
            field=models.CharField(default='your_default_value', max_length=255),
        ),
        migrations.AlterField(
            model_name='listing',
            name='lot_size',
            field=models.DecimalField(decimal_places=1, max_digits=5),
        ),
    ]