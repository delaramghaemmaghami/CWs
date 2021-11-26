from django.db import models


class TodoListItem(models.Model):
    content = models.CharField(max_length=100)

    def __str__(self):
        return self.content
