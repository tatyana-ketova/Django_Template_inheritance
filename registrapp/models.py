from django.db import models


# Create your models here.
class UserModel(models.Model):
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    mobile = models.IntegerField()
