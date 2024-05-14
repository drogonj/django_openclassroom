from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    CREATOR = 'CREATOR'
    SUBSCRIBER = 'SUBSCRIBER'
    ROLE_CHOICES = {
        (CREATOR, 'Createur'),
        (SUBSCRIBER, 'Abonne'),
    }

    profile_picture = models.ImageField()
    role = models.CharField(max_length=30, choices=ROLE_CHOICES)
