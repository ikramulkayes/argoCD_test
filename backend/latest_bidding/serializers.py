# serializers.py

from rest_framework import serializers
from .models import React



class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = React
        fields = ['post_id', 'max_price', 'current_price', 'last_bidder', 'bidding_ended']


