from django.db import models
from django.db.models import Model
from django.forms import IntegerField, FloatField, CharField

# Create your models here.

class item1 (models.Model):
    ins_municipal1 = models.FloatField()
  
class item2 (models.Model):
    ins_municipal2 = models.FloatField()    

