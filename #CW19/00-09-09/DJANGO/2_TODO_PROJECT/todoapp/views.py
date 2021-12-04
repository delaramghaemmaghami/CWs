from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView
from .models import *


class TodoList(ListView):
    model = TodoListItem
    template_name = "todoapp/todolistitem_list.html"


def add_todo_view(request):
    if request.method == "POST":
        x = request.POST.get("content")
        form_ist = AddTask(x)
        form_ist.save()
    return render(request, "pages/contact.html")


def delete_todo_view(request, i):
    y = TodoListItem.objects.get(id=i)
    y.delete()
    return HttpResponseRedirect("")
