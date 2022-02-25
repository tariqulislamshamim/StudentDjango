
from datetime import date
from django.db import models


# Create your models here.
class Student(models.Model):
    sroll= models.IntegerField(unique=True)
    sname= models.CharField(max_length=20)
    sclass = models.CharField(max_length=4)
    ssection = models.CharField(max_length=1)
    sabsent=models.IntegerField(blank=True, default=0)
    sphone= models.CharField(max_length=11, unique=True)
    pradress= models.CharField(max_length=300)
    pmadress= models.CharField(max_length=300)
    class Meta:
        ordering = ['sroll']

class AbsentDate(models.Model):
    absdate= models.DateField()
    abstudent=models.ForeignKey(Student, on_delete=models.CASCADE)   
    
