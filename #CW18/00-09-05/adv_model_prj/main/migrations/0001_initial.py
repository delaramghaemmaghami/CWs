# Generated by Django 3.2.9 on 2021-11-26 08:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(db_column='first_name', max_length=20, verbose_name='first_name')),
                ('phone', models.CharField(db_index=True, max_length=15)),
                ('person_degree', models.CharField(choices=[('dip', 'diploma'), ('mas', 'master'), ('dc', 'doctorate')], default='diploma', max_length=3)),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(18), django.core.validators.MaxValueValidator(50)])),
            ],
        ),
    ]
