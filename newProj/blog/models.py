from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    name = models.TextField()
    comment = models.TextField()
    upVote = models.IntegerField(null=True)
    downVote = models.IntegerField(null = True)
    