from django.db import models

# Create your models here.


class Marks(models.Model):
    marks = models.IntegerField()
    student = models.OneToOneField(
        'Student', on_delete=models.CASCADE, related_name='marks')

    def __str__(self):
        return f"Id:{self.id} Name: {self.student.name} Marks:{self.marks}"


class Student(models.Model):
    name = models.CharField(max_length=50, unique=True)
    standard = models.IntegerField()
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"Name: {self.name} Standard: {self.standard} City: {self.city} "
