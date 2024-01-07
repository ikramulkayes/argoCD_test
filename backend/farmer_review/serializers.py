# serializers.py

from rest_framework import serializers
from .models import React

class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = React
        fields = ['rid', 'userid','businessman_userid', 'review_content','star','product_id']
        

