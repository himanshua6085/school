from django.core.validators import MinValueValidator
from django.db import models


class Classroom(models.Model):
    name = models.CharField(max_length=10)
    seating_capacity = models.IntegerField(
        validators=[
            MinValueValidator(1)
        ]
    )


    SHAPES = (
        ('O', 'Oval'),
        ('R', 'Rectangle'),
        ('C', 'Canopy'),
        ('E', 'Elevated'),
    )

    shape = models.CharField(
        max_length=1,
        choices=SHAPES
    )

    web_lecture_support = models.BooleanField()

    def __str__(self):
        return self.name
