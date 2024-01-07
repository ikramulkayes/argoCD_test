# serializers.py

from rest_framework import serializers
from .models import FoodInventory, FoodItem

class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = ['type', 'quantity', 'quality']

class FoodInventorySerializer(serializers.ModelSerializer):
    items = FoodItemSerializer(many=True)

    class Meta:
        model = FoodInventory
        fields = ['user_id', 'district', 'division', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        food_inventory = FoodInventory.objects.create(**validated_data)

        for item_data in items_data:
            # Use set() to add items to the ManyToManyField
            food_item = FoodItem.objects.create(**item_data)
            food_inventory.items.add(food_item)

        return food_inventory
