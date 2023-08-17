from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    inventory = models.SmallAutoField()

    def __str__(self):
        return f'title: {self.title}, author: {self.author}'

    class Meta:
        # create price indexes
        indexes = models.Index(fields=['price']),
