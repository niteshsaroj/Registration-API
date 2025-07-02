from django.db import models

# Create your models here.
class UserProfile(models.Model):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username