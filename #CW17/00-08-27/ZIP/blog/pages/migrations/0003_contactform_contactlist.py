# Generated by Django 3.2.9 on 2021-11-18 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_articles'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('title', models.CharField(max_length=120)),
                ('message', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ContactList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.TextField(max_length=200)),
                ('phone', models.CharField(max_length=100)),
                ('telegram', models.CharField(max_length=100)),
            ],
        ),
    ]
