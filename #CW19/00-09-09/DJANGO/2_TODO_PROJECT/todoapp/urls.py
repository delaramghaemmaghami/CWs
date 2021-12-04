from django.urls import path
from .views import *


urlpatterns = [
    path("", TodoList.as_view(), name="todoList"),
    path("addTodoItem/", add_todo_view),
    path('deleteTodoItem/<int:i>/', delete_todo_view),
]
