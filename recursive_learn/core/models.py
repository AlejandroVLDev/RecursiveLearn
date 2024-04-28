from django.db import models
from django.contrib.auth.models import User

from exercises.models import Exercise


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    exercises = models.ManyToManyField(Exercise)
    code_change = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.user.username
