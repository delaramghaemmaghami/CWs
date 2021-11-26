from django.db import models
from django.core.validators import *
from datetime import *


class Person(models.Model):
    f_name = models.CharField(max_length=20,
                              db_column="first_name",
                              verbose_name="first_name")

    phone = models.CharField(db_index=True,
                             max_length=15)

    educational_degree = [
        ("dip", "diploma"),
        ("mas", "master"),
        ("dc", "doctorate")
    ]
    person_degree = models.CharField(choices=educational_degree,
                                     default="diploma",
                                     max_length=3)

    age = models.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(50)],
                              help_text="Your age should be between 18 and 50")

    def __str__(self):
        return self.f_name


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    today_time = models.TimeField()  # default=datetime.now()
    today_date = models.DateField()

    def __str__(self):
        return self.created
