# Generated by Django 4.2.2 on 2023-07-22 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_products_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='desc',
            new_name='description',
        ),
    ]
