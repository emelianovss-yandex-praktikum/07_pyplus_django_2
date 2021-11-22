from django.db import models


class Shape(models.Model):
    SQUARE = 'S'
    CIRCLE = 'C'

    KINDS = (
        (SQUARE, 'Квадрат'),
        (CIRCLE, 'Круг')
    )

    color = models.CharField(max_length=6)
    kind = models.CharField(max_length=1, choices=KINDS)
    draw = models.ForeignKey('draw.Draw', on_delete=models.CASCADE)
