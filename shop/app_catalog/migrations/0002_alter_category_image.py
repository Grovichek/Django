# Generated by Django 4.2.3 on 2023-08-13 08:15

import app_catalog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to=app_catalog.models.directory_path),
        ),
    ]
