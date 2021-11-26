from django.urls import path
from .views import *

urlpatterns = [
    path("todoList/", TodoList.as_view(), name="todoList"),
    path("addTodoList/", addTodoView)
]
