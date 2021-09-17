from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    contact=models.BigIntegerField()
class picture(models.Model):
    name=models.CharField(max_length=100)
    contact=models.BigIntegerField()
    place=models.CharField(max_length=100)
    image=models.CharField(max_length=100)
class details(models.Model):
    Name=models.CharField(max_length=100)
    Contact=models.BigIntegerField()
    Place=models.CharField(max_length=100)
   


