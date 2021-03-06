# Generated by Django 3.1.5 on 2021-01-13 20:21

from django.db import migrations
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_property_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='location',
            field=location_field.models.plain.PlainLocationField(default=1, max_length=63),
            preserve_default=False,
        ),
    ]
