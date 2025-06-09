from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):

    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    username = models.CharField(max_length=120 ,unique=True)
    phone = models.CharField(max_length=120)
    password = models.CharField(max_length=120)
    email = models.EmailField(unique=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures', null=True)

    def __str__(self):
        return self.username