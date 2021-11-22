from django.db import models


class Draw(models.Model):
    title = models.CharField(max_length=32)


class Album(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    draws = models.ManyToManyField(Draw, blank=True)
