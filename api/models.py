from django.db import models

# Create your models here.


class Hero(models.Model):
    name = models.TextField(default='')