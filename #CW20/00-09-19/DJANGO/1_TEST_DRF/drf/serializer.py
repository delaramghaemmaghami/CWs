from .models import *
from rest_framework import serializers


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        # fields = "__all__"
        fields = ["name"]
