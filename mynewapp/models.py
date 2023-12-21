from django.db import models


class Position(models.Model):
    title = models.CharField(max_length=50)




class Employee(models.Model):
    full_name = models.CharField(max_length=50)
    emp_code = models.CharField(max_length=20)
    mobile = models.CharField(max_length=15)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)