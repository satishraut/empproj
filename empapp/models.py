from django.db import models
 

# Create your models here.

class Employee(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField()
    salary=models.IntegerField()
    country=models.CharField(max_length=20, default='Checking')

    class Meta:
        db_table="Emp_Info"




