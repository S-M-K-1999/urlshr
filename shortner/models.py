from django.db import models
from django.db.models.base import Model

# Create your models here.
class urls(models.Model):
    link=models.CharField(max_length=100000)
    uid=models.CharField(max_length=20)