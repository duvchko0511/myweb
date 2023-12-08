from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Nevtreh(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField()
    last_name = models.TextField()
    location = models.CharField(max_length=100, blank=True)
    age = models.IntegerField()
    bio = models.TextField(blank= True)

    def __str__(self):
        return self.user.username
    