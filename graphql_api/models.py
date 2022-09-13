from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=255,)
    followers = models.ManyToManyField('self',)
