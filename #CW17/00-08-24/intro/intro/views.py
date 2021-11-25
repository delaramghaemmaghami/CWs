from django.http import HttpResponse
from django.shortcuts import render


def about_page(requests):
    return HttpResponse("Hello this is about page!")


def random_page(requests):
    return render(requests, "index.html")
