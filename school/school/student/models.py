from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from subject.models import Subject


class Student(models.Model):
    name = models.CharField(max_length=50)
    date_of_joining = models.DateField()
    standard = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(12)
        ]
    )
    roll_no = models.IntegerField(
        unique=True,
        validators=[
            MinValueValidator(1)
        ]
    )
    subjects = models.ManyToManyField(Subject)

    def __str__(self):
        return self.name


class Relative(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField(
        validators=[
            MinValueValidator(7 * 10**9),
            MaxValueValidator(10**10 - 1)
        ]
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    RELATIONS = (
        ('F', 'Father'),
        ('M', 'Mother'),
        ('G', 'Guardian'),
        ('O', 'Other'),
    )
    relation = models.CharField(max_length=1, choices=RELATIONS)

    def __str__(self):
        return self.name