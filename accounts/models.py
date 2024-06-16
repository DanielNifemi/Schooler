from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)


class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    # Add more fields as needed

    def __str__(self):
        return f"{self.user.username} - Teacher"


class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    grade = models.CharField(max_length=20, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    major = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    # Add more fields as needed

    def __str__(self):
        return f"{self.user.username} - Student"
