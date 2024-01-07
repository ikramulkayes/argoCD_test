from django.shortcuts import render
from rest_framework.views import APIView
from .models import React
from .serializers import ReactSerializer  # Adjusted import
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

class ReactView_Register_latest_bidding(APIView):
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

class CheckUserExistenceView_latest_bidding(APIView):
    def post(self, request):
        post_id = request.data.get('post_id')

        # Check if users with the given userid exist
        users = React.objects.filter(post_id=post_id)

        if users.exists():
            # At least one user with the given userid exists
            user_data = users.values('post_id', 'max_price', 'current_price', 'last_bidder', 'bidding_ended')
            response_data = {
                "post_id": post_id,
                "exists": True,
                "user_data": user_data[0],  # Take the first user's data
            }
            print(user_data[0]['post_id'])
        else:
            response_data = {"post_id": post_id, "exists": False, "user_data": {}}

        return Response(response_data)

class ReactView_DeleteMember_latest_bidding(APIView):
    def post(self, request):
        post_id = request.data.get('post_id')
        print(post_id)

        try:
            member = React.objects.get(post_id=post_id)
            member.delete()
            return Response({'success': True})
        except React.DoesNotExist:
            return Response({'success': False, 'error': 'Member does not exist'})

class ReactView_Edit_latest_bidding(APIView):
    def post(self, request):
        serializer = ReactSerializer(data=request.data)  # Adjusted serializer
        if serializer.is_valid():
            post_id = request.data.get('post_id', '')
            react_instance = get_object_or_404(React, post_id=post_id)

            # Update the object with new data
            react_instance.max_price = request.data.get('max_price', react_instance.max_price)
            react_instance.current_price = request.data.get('current_price', react_instance.current_price)
            react_instance.last_bidder = request.data.get('last_bidder', react_instance.last_bidder)
            react_instance.bidding_ended = request.data.get('bidding_ended', react_instance.bidding_ended)


            # Save the changes
            react_instance.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReactView_Edit_latest_bidding_ended(APIView):
    def post(self, request):

            post_id = request.data.get('post_id', '')
            react_instance = get_object_or_404(React, post_id=post_id)
            
            # Update the object with new data
            
            react_instance.bidding_ended = request.data.get('bidding_ended', react_instance.bidding_ended)


            # Save the changes
            react_instance.save()

            return Response(status=status.HTTP_201_CREATED)

class ReactView_Edit_latest_bidding_maxprice(APIView):
    def post(self, request):

            post_id = request.data.get('post_id', '')
            react_instance = get_object_or_404(React, post_id=post_id)
            
            # Update the object with new data
            
            react_instance.max_price = request.data.get('max_price', react_instance.bidding_ended)


            # Save the changes
            react_instance.save()

            return Response(status=status.HTTP_201_CREATED)

        
