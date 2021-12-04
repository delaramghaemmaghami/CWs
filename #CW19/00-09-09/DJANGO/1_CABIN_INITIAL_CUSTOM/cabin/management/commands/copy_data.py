import json

from django.core.management import BaseCommand

from cabin.models import *


class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        f = open('sample_test_fixture.json', )
        data = json.load(f)
        for i in data:

            # if i.get('model') == 'cabin.account':
            #     Account.objects.get_or_create(pk=i.get('pk'), defaults={
            #         "first_name": i.get('fields')['first_name'],
            #         "last_name": i.get('fields')['last_name'],
            #         "email": i.get('fields')['email'],
            #         "password": i.get('fields')['password'],
            #         "content_type": ContentType.objects.get(id=i.get('fields')['content_type']),
            #         "object_id": i.get('fields')['object_id']
            #     })
            # elif i.get('model') == 'cabin.rider':
            #     Rider.objects.get_or_create(pk=i.get('pk'), defaults={
            #         "rating": i.get('fields')['rating'],
            #         "x": i.get('fields')['x'],
            #         "y": i.get('fields')['y']
            #     })
            # elif i.get('model') == 'cabin.driver':
            #     Driver.objects.get_or_create(pk=i.get('pk'), defaults={
            #         "rating": i.get('fields')['rating'],
            #         "x": i.get('fields')['x'],
            #         "y": i.get('fields')['y'],
            #         "active": i.get('fields')["active"]
            #     })
            # elif i.get('model') == 'cabin.riderequest':
            #     RideRequest.objects.get_or_create(pk=i.get('pk'), defaults={
            #         "rider": Rider.objects.get(id=i.get('fields')['rider']),
            #         "car_type": i.get('fields')['car_type'],
            #         "x": i.get('fields')['x'],
            #         "y": i.get('fields')['y'],
            #     })
            # if i.get('model') == 'cabin.car':
            #     Car.objects.get_or_create(pk=i.get('pk'), defaults={
            #         "owner": Driver.objects.get(id=i.get('fields')['owner']),
            #         "car_type": i.get('fields')['car_type'],
            #         "model": i.get('fields')['model'],
            #         "color": i.get('fields')['color'],
            #     })
            # if i.get('model') == 'cabin.ride':
            #     Ride.objects.get_or_create(pk=i.get('pk'), defaults={
            #         "pickup_time": i.get('fields')['pickup_time'],
            #         "dropoff_time": i.get('fields')['dropoff_time'],
            #         "rider_rating": i.get('fields')['rider_rating'],
            #         "driver_rating": i.get('fields')['driver_rating'],
            #         "car": Car.objects.get(id=i.get('fields')['car']),
            #         "request": RideRequest.objects.get(id=i.get('fields')['request']),
            #     })
            if i.get('model') == 'cabin.payment':
                Payment.objects.get_or_create(pk=i.get('pk'), defaults={
                    "ride": Ride.objects.get(id=i.get('fields')['ride']),
                    "amount": i.get('fields')['amount'],
                    "status": i.get('fields')['status'],
                })
