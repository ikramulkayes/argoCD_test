from django.shortcuts import render
from rest_framework.views import APIView
from .models import React
from .serializers import ReactSerializer  # Adjusted import
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from decimal import Decimal
from django.db.models import Avg

class ReactView_Register_farmer_review(APIView):
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
    

class ReactView_Search_farmer_review(APIView):
    def post(self, request):
        # Get the search parameters from the request
        userid = request.data.get('userid')
        print(userid)

        # Filter the queryset based on userid
        queryset = React.objects.filter(userid=userid)

        # Check if there are reviews for the given userid
        if queryset.exists():
            # Calculate the average star rating using Django's Avg aggregation function
            average_star = queryset.aggregate(Avg('star'))['star__avg']

            # Return the average star rating
            return Response({'average_star': average_star})
        else:
            # No reviews found for the given userid
            return Response({'average_star': 0})

