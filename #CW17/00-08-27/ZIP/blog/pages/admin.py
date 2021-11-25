from django.contrib import admin
from .models import Person, articles,  ContactList, ContactForm

# Register your models here.
admin.site.register(Person)
admin.site.register(articles)
admin.site.register(ContactForm)
admin.site.register(ContactList)