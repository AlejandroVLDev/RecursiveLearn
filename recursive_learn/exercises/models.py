from django.db import models


class Exercise(models.Model):
    NAME_MAX_LENGTH = 50
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    difficulty = models.IntegerField(default=1)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
