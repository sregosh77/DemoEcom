# Generated by Django 4.2.2 on 2023-08-02 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_alter_cart_cart_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='cart_id',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
