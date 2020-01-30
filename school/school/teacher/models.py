from django.core.validators import MinValueValidator
from django.db import models

from subject.models import Subject


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    date_of_joining = models.DateField()
    subjects = models.ManyToManyField(Subject)
    salary = models.FloatField(
        validators=[
            MinValueValidator(1.0)
        ]
    )
    web_lecture_support = models.BooleanField(default=False)

    def __str__(self):
        return self.name
