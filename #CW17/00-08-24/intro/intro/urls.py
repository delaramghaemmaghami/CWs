from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("about/", about_page),
    path("har-esmi/", random_page)
]
