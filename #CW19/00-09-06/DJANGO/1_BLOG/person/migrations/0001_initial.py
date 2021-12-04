# Generated by Django 3.2.9 on 2021-11-27 16:12

import colorfield.fields
from django.db import migrations, models
import person.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('phone', models.CharField(max_length=15)),
                ('location', models.CharField(max_length=200)),
                ('about_store', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to=person.models.Good.get_upload_path)),
                ('price', models.IntegerField()),
                ('color', colorfield.fields.ColorField(default='black', max_length=18)),
                ('factory_date', models.DateField()),
                ('store_name', models.ManyToManyField(to='person.Store')),
            ],
        ),
    ]
