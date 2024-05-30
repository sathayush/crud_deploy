from django.db import models

# Create your models here.
class Student(models.Model):
    Name=models.CharField(max_length=45)
    age=models.IntegerField()
    class Meta:
        db_table='student'



class Teacher(models.Model):
    Name=models.CharField(max_length=45)
    age=models.IntegerField()
    class Meta:
        db_table='teacher'   



       

