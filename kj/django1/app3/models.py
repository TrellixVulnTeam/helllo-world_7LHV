from django.db import models

# Create your models here.
class Person(models.Model):
    user = models.CharField(max_length=30)
    age = models.IntegerField()