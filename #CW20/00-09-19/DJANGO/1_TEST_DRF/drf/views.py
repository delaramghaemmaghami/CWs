from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
from .models import Person


class HelloApi(APIView):
    def get(self, *args, **kwargs):
        return Response(
            {"Hello": "Hello to everyOne!"},
            status=200
        )


class PersonApi(APIView):
    def get(self,request, *args, **kwargs):
        all_persons = Person.objects.all()

        all_person_serializer = PersonSerializer(all_persons, many=True)

        return Response({"persons": all_person_serializer.data})
