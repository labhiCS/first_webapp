from django.db import models

# Create your models here.

class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.Date