from turtle import title
from unicodedata import category
from django.db import models
from django.utils import timezone



class Category(models.Model):
    category = models.CharField(max_length=30)

class Restaurant(models.Model):
    title = models.CharField(max_length=100)
    lucations = models.FloatField(max_length=50)
    

# Create your models here.
