from django.db import models

class Class(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    full_name = models.CharField(max_length=255)
    price = models.FloatField(default=0)
    clas = models.ManyToManyField(Class)

    def __str__(self):
        return self.full_name


class Student(models.Model):
    full_name = models.CharField(max_length=255)
    clas = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name



