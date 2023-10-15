from django.db import models

# Create your models here.
class Hashtag(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=200)