from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField("Date Added")
    def __str__(self) -> str:
        return self.name

class Club(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    icon = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.name

class Student(models.Model):
    clubs = models.ManyToManyField(Club)
    name = models.CharField(max_length=200)
    icon = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.name