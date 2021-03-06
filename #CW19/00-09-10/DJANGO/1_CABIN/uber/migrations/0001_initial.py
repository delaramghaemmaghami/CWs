# Generated by Django 3.2.9 on 2021-12-01 17:26

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator('09(1[0-9]|3[1-9]|2[1-9])-?[0-9]{3}-?[0-9]{4}', message='Please enter a valid phone number!')])),
                ('password', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_type', models.CharField(choices=[('A', 'class A'), ('B', 'class B'), ('C', 'class C')], default='class A', max_length=10)),
                ('model', models.IntegerField(validators=[django.core.validators.MaxValueValidator(2021), django.core.validators.MinValueValidator(2015)])),
                ('color', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Rider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.FloatField(db_column='Longitude', verbose_name='Longitude')),
                ('y', models.FloatField(db_column='Latitude', verbose_name='Latitude')),
                ('rating', models.IntegerField()),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='uber.account')),
            ],
        ),
        migrations.CreateModel(
            name='RideRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
                ('car_type', models.CharField(choices=[('A', 'class A'), ('B', 'class B'), ('C', 'class C')], max_length=1, verbose_name='car type')),
                ('rider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uber.rider')),
            ],
        ),
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickup_time', models.PositiveIntegerField()),
                ('drop_off_time', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('rider_rating', models.CharField(max_length=10, verbose_name=[('perfect', 'Perfect'), ('very_good', 'Very Good'), ('good', 'Good'), ('bad', 'Bad'), ('very_bad', 'Very Bad')])),
                ('driver_rating', models.CharField(max_length=10, verbose_name=[('perfect', 'Perfect'), ('very_good', 'Very Good'), ('good', 'Good'), ('bad', 'Bad'), ('very_bad', 'Very Bad')])),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uber.car')),
                ('request', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='uber.riderequest')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('status', models.BooleanField(default=False)),
                ('ride', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uber.ride')),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.FloatField(verbose_name='longitude')),
                ('y', models.FloatField(verbose_name='latitude')),
                ('rating', models.CharField(choices=[('perfect', 'Perfect'), ('very_good', 'Very Good'), ('good', 'Good'), ('bad', 'Bad'), ('very_bad', 'Very Bad')], max_length=9)),
                ('active', models.BooleanField(default=False)),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='uber.account')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uber.driver'),
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='uber.account')),
            ],
        ),
    ]
