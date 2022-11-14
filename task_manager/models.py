from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    text = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    done = models.BooleanField()
    tags = models.ManyToManyField(Tag, related_name="tasks")

    def __str__(self):
        return self.text