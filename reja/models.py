from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    ism = models.CharField(max_length=30)
    guruh = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.ism


class Reja(models.Model):
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=30, blank=False)
    vaqt = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=300)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.title









