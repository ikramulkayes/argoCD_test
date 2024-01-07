# authentication/serializers.py
from rest_framework import serializers
from .models import *

class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = React
        fields = ['userid', 'password','email','address','nid','user_type']
       


