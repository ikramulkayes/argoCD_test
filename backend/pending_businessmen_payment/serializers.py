# serializers.py

from rest_framework import serializers
from .models import React

class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = React
        fields = ['post_id', 'name', 'amount', 'price', 'businessman_userid', 'farmer_userid','location']
