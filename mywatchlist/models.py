from django.db import models

# Create your models here.
class MyWatchList(models.Model):
    watched = models.BooleanField(default=False)
    title = models.TextField()
    rating = models.IntegerField()
    release_date = models.IntegerField()
    review = models.TextField()
