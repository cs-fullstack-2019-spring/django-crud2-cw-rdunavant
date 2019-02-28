from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=256, unique=True)
    phoneNumber = models.IntegerField()

def __str__(self):
        return self.first_name