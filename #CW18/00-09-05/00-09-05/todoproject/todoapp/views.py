from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import *
from .models import *


class TodoList(ListView):
    model = TodoListItem
    template_name = "todoapp_list.html"


def addTodoView(request):
    x = request.POST['content']
    new_item = TodoListItem(content=x)
    new_item.save()
    return HttpResponseRedirect('/todoapp/')
