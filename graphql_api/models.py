from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=255,)
    followers = models.ManyToManyField('self',)


class Post(models.Model):
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
