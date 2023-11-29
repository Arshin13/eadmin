from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=200)
    department=models.CharField(max_length=200)

    class Meta:
        db_table='employee_tb'

class Login(models.Model):
    uname=models.CharField(max_length=200)
    password=models.CharField(max_length=200)

    class Meta:
        db_table='login_tb'


