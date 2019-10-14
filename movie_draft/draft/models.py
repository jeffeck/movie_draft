from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=250)
    stats_url = models.URLField() 
    release_date = models.DateField() 

