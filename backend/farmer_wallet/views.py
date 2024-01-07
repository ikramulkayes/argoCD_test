from django.shortcuts import render
from rest_framework.views import APIView
from .models import React
from .serializers import ReactSerializer  # Adjusted import
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from decimal import Decimal

class ReactView_Register_farmer_wallet(APIView):
    def get(self, request):
        data = React.objects.all()
        serializer = ReactSerializer(data, many=True)  # Adjusted serializer
        return Response(serializer.data)

    def post(self, request):
        serializer = ReactSerializer(data=request.data)  # Adjusted serializer
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ReactView_Search_farmer_wallet(APIView):
    def post(self, request):
        # Get the search parameters from the request
        userid = request.data.get('userid')
        print(userid)

        # Initialize a queryset with all objects
        queryset = React.objects.all()
        print(userid)
        # Perform search operations
        if userid:
            queryset = queryset.filter(userid=userid)
            print(queryset)
        




        # Serialize the filtered queryset
        serializer = ReactSerializer(queryset, many=True)

        return Response(serializer.data[0])

class ReactView_Update_farmer_wallet(APIView):
    def post(self, request):
        post_id = request.data.get('userid')
        delivery_state = request.data.get('price')
        print(post_id,delivery_state)

        try:
            # Get the React instance with the specified post_id
            react_instance = React.objects.get(userid=post_id)

            # Update the delivery_state
            react_instance.total_money = react_instance.total_money + Decimal(str(delivery_state))
            react_instance.save()

            # Serialize the updated instance
            serializer = ReactSerializer(react_instance)

            return Response(serializer.data)
        except React.DoesNotExist:
            # If the React instance with the specified post_id does not exist
            print("Error")