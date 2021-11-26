from django.shortcuts import render


def home(requests):
    context = {
        "test": "hi", 
        "name": "delaram", 
        "age": 24, 
        "style": "color:red",
        "friends": [
            "kimia", 
            "azin", 
            "atiyeh", 
            "sarina"
        ]
    }
    return render(requests, "home.html", context)


def about(requests):
    return render(requests, "about.html")
