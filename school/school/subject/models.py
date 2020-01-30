from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from classroom.models import Classroom


class Subject(models.Model):
    name = models.CharField(max_length=50)
    chapters = models.IntegerField(
        validators=[
            MinValueValidator(1)
        ]
    )
    total_duration = models.IntegerField(
        validators=[
            MinValueValidator(30)
        ]
    )
    duration_per_class = models.IntegerField(
        validators=[
            MinValueValidator(30),
            MaxValueValidator(120)
        ]
    )
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
