from django.urls import path
from .views import *


urlpatterns = [
    path("api/hello/", HelloApi.as_view()),
    path("api/persons/", PersonApi.as_view())
]
