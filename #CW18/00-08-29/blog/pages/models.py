from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Article(models.Model):
    title = models.CharField(max_length=50)
    test_field = models.TextField(max_length=500)

    def __str__(self):
        return self.title + " " + self.test_field
