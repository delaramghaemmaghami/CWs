from .models import *
import math
from django.db.models import Sum


def query_0(x):
    a = Driver.objects.filter(rating__gte=x).all()
    return a


def query_1(x):
    # payments = Payment.objects.filter(ride__car__owner_id=x).all()

    # result = 0
    #
    # for payment in payments:
    #     result += payment.amount

    # return result

    # second way
    payments1 = Payment.objects.filter(ride__car__owner_id=x).aggregate(sum_amount=Sum("amount"))
    print(payments1)


def query_2(x):
    a = Ride.objects.filter(request__rider_id=x).all()
    return a


def query_3(x, y, r):
    drivers = Driver.objects.filter(active=True).all()

    far_drivers = []

    for driver in drivers:
        if math.sqrt((x - driver.x) ** 2 + (y - driver.y) ** 2) > r:
            far_drivers.append(driver.id)

    return drivers.exclude(id__in=far_drivers)


def query_4(c):
    a = Driver.objects.filter(cars__color=c).all()
    return a


def query_5(c):
    a = Driver.objects.filter(cars__color=c, cars__car_type="A")
    return a
