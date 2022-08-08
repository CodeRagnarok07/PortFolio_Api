from email.mime import image
from statistics import mode
from django.db import models

# Create your models here.


class Skills(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()
    description = models.TextField()