from django.db import models

# Create your models here.
from django.contrib.auth.models import User 

class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    inventory = models.SmallIntegerField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)

    def __str__(self):
        return f'title: {self.title}, author: {self.author}'

    class Meta:
        # create price indexes
        indexes = models.Index(fields=['price']),


class Rating(models.Model):
    menuitem_id = models.SmallIntegerField()
    rating = models.SmallIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
