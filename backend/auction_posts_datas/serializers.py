# serializers.py

from rest_framework import serializers
from .models import AuctionsInventory



class AuctionsInventorySerializer(serializers.ModelSerializer):
   

    class Meta:
        model = AuctionsInventory
        fields = ['post_id', 'name', 'amount', 'price', 'total_bidding_placed', 'start_time', 'end_time', 'current_time','posted_by', 'description']


