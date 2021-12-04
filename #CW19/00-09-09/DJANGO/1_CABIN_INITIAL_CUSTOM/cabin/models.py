from colorfield.fields import ColorField
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator
from django.db import models

RATING_CHOICES = [
        ('perfect', 'Perfect'),
        ('very_good', 'Very Good'),
        ('good', 'Good'),
        ('bad', 'Bad'),
        ('very_bad', 'Very Bad')
]

car_type_choices = (
    ('A', 'class A'),
    ('B', 'class B'),
    ('C', 'class C'),
)

PHONE_REGEX = RegexValidator("09(1[0-9]|3[1-9]|2[1-9])-?[0-9]{3}-?[0-9]{4}",
                             message="Please enter a valid phone number!")


class Account(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, validators=[PHONE_REGEX])
    password = models.CharField(max_length=10)


class Admin(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE)


class Rider(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    x = models.FloatField(verbose_name="Longitude", db_column="Longitude")
    y = models.FloatField(verbose_name="Latitude", db_column="Latitude")
    rating = models.IntegerField()


class Driver(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    x = models.FloatField(verbose_name="longitude")
    y = models.FloatField(verbose_name="latitude")

    # There's no number in rating choices, so why IntegerField?
    rating = models.IntegerField(choices=RATING_CHOICES)

    active = models.BooleanField(default=False)


class RideRequest(models.Model):
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE)
    x = models.FloatField()
    y = models.FloatField()
    car_type = models.CharField(choices=car_type_choices, max_length=1, verbose_name='car type')


class Car(models.Model):
    owner = models.ForeignKey(Driver, on_delete=models.CASCADE)
    car_type = models.CharField(Choices=car_type_choices, max_length=10, default="class A")
    model = models.IntegerField(validators=[MaxValueValidator(2021), MinValueValidator(2015)])
    color = ColorField(default="black")


class Ride(models.Model):
    pickup_time = models.PositiveIntegerField()
    drop_off_time = models.IntegerField(validators=[MinValueValidator(0)])
    request = models.OneToOneField(RideRequest, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    rider_rating = models.Choices(RATING_CHOICES)
    driver_rating = models.Choices(RATING_CHOICES)


class Payment(models.Model):
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE)
    amount = models.FloatField()
    status = models.BooleanField(default=False)
