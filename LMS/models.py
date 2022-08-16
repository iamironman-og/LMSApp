from datetime import date
from enum import unique
from importlib.resources import path
from lib2to3.pgen2.literals import evalString
from pyexpat import model
from tkinter import Widget
from unittest.util import _MAX_LENGTH
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime

# Create your models here.
# username-admin password-Admin@123
class Instructor(models.Model):
    InstructorId = models.AutoField(primary_key=True)
    InstructorName = models.CharField(max_length=100)
    InstructorEmailId = models.EmailField(unique=True, max_length=500)
    # InstructorPassword = models.CharField(max_length=100)
    InstructorMobileNo = PhoneNumberField(null=False, blank=False, unique=True)
    path = "Instructor//Profile//1"
    InstructorPhoto = models.FileField(upload_to=path)


class Subject(models.Model):
    subjectId = models.AutoField(primary_key=True)
    subjectName = models.CharField(max_length=100)
    Instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
# Student s1,s2,s3,s4;
# Enrollment e1;
# e1.subject(BDA)
# e1.


class Student(models.Model):
    studentId = models.AutoField(primary_key=True)
    studentName = models.CharField(max_length=100)
    studentEmailId = models.EmailField(unique=True)
    # studentPassword = models.CharField(max_length=20)
    studentDOB = models.DateField()
    path = "Student//Profile//1"
    studentProfile = models.FileField(upload_to=path)
    studentMobileNo = PhoneNumberField(null=False, blank=False, unique=True)


class Enrollment(models.Model):
    enrollmentId = models.AutoField(primary_key=True)
    # academicYear = models.DateTimeField(datetime.today())
    enrolledStudents = models.ManyToManyField(Student)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
