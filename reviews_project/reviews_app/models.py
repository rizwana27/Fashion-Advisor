from django.db import models

class Review(models.Model):
    name = models.CharField(max_length=200)
    review = models.TextField()
    rating = models.IntegerField()