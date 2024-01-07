# models.py

from django.db import models

class FoodItem(models.Model):
    type = models.CharField(max_length=255)
    quantity = models.IntegerField()
    quality = models.IntegerField()

    class Meta:
        db_table = 'bloglist_fooditems'  

class FoodInventory(models.Model):
    user_id = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    division = models.CharField(max_length=255)
    items = models.ManyToManyField(FoodItem, related_name='food_inventory')

    class Meta:
        db_table = 'bloglist_inventory'
