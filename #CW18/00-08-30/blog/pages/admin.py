from django.contrib import admin
from .models import Person, articles, ContactForm, ContactList

# Register your models here.
admin.site.register(Person)
admin.site.register(articles)
admin.site.register(ContactList)
admin.site.register(ContactForm)
