# Generated by Django 3.1.5 on 2021-01-05 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='property.category'),
        ),
    ]
