# serializers.py

from rest_framework import serializers
from .models import React

class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = React
        fields = ['pending_payment_id', 'userid', 'transaction_id', 'price', 'product_id', 'name', 'location']

