# Generated by Django 4.1.7 on 2023-03-22 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(default='имя не присвоено', max_length=128, unique=True)),
                ('category_picture', models.ImageField(upload_to='images/')),
            ],
            options={
                'verbose_name': 'Каталог',
                'verbose_name_plural': 'Каталоги',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('phone', models.CharField(max_length=20, unique=True)),
                ('email', models.EmailField(max_length=30, unique=True)),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200, unique=True)),
                ('product_ves', models.IntegerField(max_length=200)),
                ('product_price', models.IntegerField(max_length=200)),
                ('product_godnost', models.IntegerField(max_length=200)),
                ('product_volume', models.IntegerField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='media/', verbose_name='изображение')),
                ('ssilka', models.URLField(default='http://127.0.0.1:8000/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APP.category')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]
