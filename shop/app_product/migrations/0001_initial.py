# Generated by Django 4.2.3 on 2023-08-12 08:29

import app_product.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('count', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=200)),
                ('full_description', models.TextField(max_length=800)),
                ('free_delivery', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ProductTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('product', models.ManyToManyField(to='app_product.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductSpecification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=100)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_product.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('text', models.TextField(max_length=400)),
                ('rate', models.IntegerField(default=5)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_product.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src', models.ImageField(upload_to=app_product.models.directory_path)),
                ('alt', models.CharField(max_length=200)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_product.product')),
            ],
        ),
    ]
