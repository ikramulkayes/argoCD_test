from django.shortcuts import render
from rest_framework.views import APIView
from .models import React
from .serializers import ReactSerializer  # Adjusted import
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

class ReactView_Register_pending_farmer_payment(APIView):
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

class ReactView_DeleteMember_pending_farmer_payment(APIView):
    def post(self, request):
        post_id = request.data.get('product_id')
        print(post_id)

        try:
            member = React.objects.get(product_id=post_id)
            member.delete()
            return Response({'success': True})
        except React.DoesNotExist:
            return Response({'success': False, 'error': 'product does not exist'})


class ReactView_Search_Sort_pending_farmer_payment(APIView):
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

        return Response(serializer.data)
    
class ReactView_Get_pending_farmer_paymentdata(APIView):
    def post(self, request):
        # Get the search parameters from the request
        userid = request.data.get('product_id')
        print(userid)

        # Initialize a queryset with all objects
        queryset = React.objects.all()
        print(userid)
        # Perform search operations
        if userid:
            queryset = queryset.filter(product_id=userid)
            print(queryset)
        




        # Serialize the filtered queryset
        serializer = ReactSerializer(queryset, many=True)

        return Response(serializer.data[0])