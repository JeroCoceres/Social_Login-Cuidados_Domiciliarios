from django.db import models

class Course(models.Model):
    courseID = models.BigAutoField(primary_key=True)
    courseName = models.CharField(max_length=255)
    courseSkill = models.CharField(max_length=255)
    courseDateTime = models.DateTimeField()

class Student(models.Model):
    studentID = models.BigAutoField(primary_key=True)
    courseID = models.ManyToManyField(Course, related_name='students')
    approved = models.BooleanField(default=False)
