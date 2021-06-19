from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from datetime import date, datetime


class Profile(models.Model):
    user = models.OneToOneField(User, null = True, on_delete=models.CASCADE)
    bio = models.TextField()
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.user)