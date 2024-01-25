from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=100)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname', 'lastname', 'username', 'password', 'role']

    def __str__(self):
        return "{}".format(self.email)
