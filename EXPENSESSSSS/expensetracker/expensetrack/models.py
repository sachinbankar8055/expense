from django.db import models

# Create your models here.


class Ade(models.Model):

    username= models.CharField(max_length=100)
    date= models.DateField(max_length=100)
    food=models.CharField(max_length=100)
    petrol=models.CharField(max_length=100)
    travel=models.CharField(max_length=100)
    movie=models.CharField(max_length=100)
    rent=models.CharField(max_length=100)
    other=models.CharField(max_length=100)