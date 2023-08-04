from django.db import models

# Create your models here.


class college(models.Model):
    CollegeID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    year = models.IntegerField(null=True)


class MenuCategory(models.Model):
    menu_category_name = models.CharField(max_length=200)


class Menu(models.Model):
    menu_item = models.CharField(max_length=200)
    price = models.IntegerField(null=False)
    category_id = models.ForeignKey(MenuCategory,
                                    on_delete=models.PROTECT,
                                    default=None,
                                    related_name="category_name")


class Logger(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    time_log = models.TimeField(help_text="hh:mm:ss")
