# Generated by Django 3.1.5 on 2021-01-05 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_property_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='property',
            options={'verbose_name': 'Property', 'verbose_name_plural': 'Properties'},
        ),
    ]
