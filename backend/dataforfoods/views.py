from django.shortcuts import render
from rest_framework.views import APIView
from .models import FoodInventory,FoodItem
from .serializers import FoodInventorySerializer,FoodItemSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

class ReactView_Register_DataForFoods(APIView):
    def get(self, request):
        data = FoodInventory.objects.all()
        serializer = FoodInventorySerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FoodInventorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)