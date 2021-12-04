from django.db import models
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator

# Create your models here.
RATING_CHOICES = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
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
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=0)


class Driver(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    x = models.FloatField(verbose_name="longitude")
    y = models.FloatField(verbose_name="latitude")
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=0)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.account.name


class RideRequest(models.Model):
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE)
    x = models.FloatField()
    y = models.FloatField()
    car_type = models.CharField(choices=car_type_choices, max_length=1, verbose_name='car type')


class Car(models.Model):
    owner = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name="cars")
    car_type = models.CharField(choices=car_type_choices, max_length=10, default="class A")
    model = models.IntegerField(validators=[MaxValueValidator(2021), MinValueValidator(2015)])
    color = models.CharField(max_length=20)

#  a = Ride.objects.filter(request__rider_id=x).all()

class Ride(models.Model):
    pickup_time = models.PositiveIntegerField()
    drop_off_time = models.IntegerField(validators=[MinValueValidator(0)])
    request = models.OneToOneField(RideRequest, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    rider_rating = models.IntegerField(choices=RATING_CHOICES, default=0)
    driver_rating = models.IntegerField(choices=RATING_CHOICES, default=0)


class Payment(models.Model):
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE)
    amount = models.FloatField()
    status = models.BooleanField(default=False)
