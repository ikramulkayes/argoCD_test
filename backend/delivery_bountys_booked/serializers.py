# serializers.py

from rest_framework import serializers
from .models import React

class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = React
        fields = ['pending_delivery_id', 'deliveryman_userid','delivery_state', 'transaction_id', 'amount', 'product_id', 'name', 'location']

