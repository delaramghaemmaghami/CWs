from django.db import models

class ContactList(models.Model):
    email = models.EmailField(blank=False, null= False , unique=True )
    address = models.TextField(max_length=200, blank=False)
    phone = models.CharField(max_length=100, blank=False)
    telegram = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.email

class ContactForm(models.Model):
    name = models.CharField(max_length=100, blank=True, unique=True, null=True)
    email = models.EmailField(blank=False)
    title = models.CharField(max_length=120, blank=False)
    message = models.TextField(max_length=500, blank=False)

    def __str__(self):
        return self.title




















# class About(models.Model):
#     title = models.CharField(max_length=100, blank=False)
#     description = models.TextField(max_length=720, blank=False)
#     # image = models.ImageField(upload_to='about/', blank=False)

#     def __str__(self):
#         return self.title




class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


    def __str__(self):
        return self.first_name +" "+ self.last_name


class articles(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField(max_length=500)

    def __str__(self):
        return self.title + "**"