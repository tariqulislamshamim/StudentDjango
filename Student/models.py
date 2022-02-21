from django.db import models


# Create your models here.
class Student(models.Model):
    sroll= models.IntegerField(max_length=2)
    sname= models.CharField(max_length=20)
    CLASS_CHOICES = (
        ('6', 'VI'),
        ('7', 'VII'),
    )
    sclass = models.CharField(max_length=1, choices=CLASS_CHOICES)
    SECTION_CHOICES = (
        ('p', 'P'),
        ('q', 'Q'),
    )
    ssection = models.CharField(max_length=1, choices=SECTION_CHOICES)
    sphone= models.CharField(max_length=11)
    pradress= models.CharField(max_length=20)
    pmadress= models.CharField(max_length=20)
    
