from django.urls import path
from .views import *


urlpatterns = [
    path('', home_page),
    path('about/', about_page),
    path('contact/us/', contact_page),
]
