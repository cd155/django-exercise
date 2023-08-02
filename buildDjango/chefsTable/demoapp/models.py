from django.db import models

# Create your models here.


class college(models.Model):
    CollegeID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
