# Generated by Django 4.2.3 on 2023-08-10 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_product', '0005_alter_productimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
