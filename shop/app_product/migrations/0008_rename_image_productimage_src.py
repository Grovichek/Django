# Generated by Django 4.2.3 on 2023-08-10 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_product', '0007_alter_product_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productimage',
            old_name='image',
            new_name='src',
        ),
    ]
