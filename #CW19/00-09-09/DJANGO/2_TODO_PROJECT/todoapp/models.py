from django.db import models


class TodoListItem(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.content


class AddTask(models.Model):
    content = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.content
