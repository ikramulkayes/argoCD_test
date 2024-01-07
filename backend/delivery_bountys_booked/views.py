from django.shortcuts import render
from rest_framework.views import APIView
from .models import React
from .serializers import ReactSerializer  # Adjusted import
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

class ReactView_Register_bounties_accepted(APIView):
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

class ReactView_DeleteMember_bounties_accepted(APIView):
    def post(self, request):
        post_id = request.data.get('product_id')
        print(post_id)

        try:
            member = React.objects.get(product_id=post_id)
            member.delete()
            return Response({'success': True})
        except React.DoesNotExist:
            return Response({'success': False, 'error': 'product does not exist'})


class ReactView_Search_Sort_bounties_accepted(APIView):
    def post(self, request):
        # Get the search parameters from the request
        userid = request.data.get('userid')
        print(userid)

        # Initialize a queryset with all objects
        queryset = React.objects.all()
        print(userid)
        # Perform search operations
        if userid:
            queryset = queryset.filter(deliveryman_userid=userid)
            print(queryset)
        




        # Serialize the filtered queryset
        serializer = ReactSerializer(queryset, many=True)

        return Response(serializer.data)


class ReactView_UpdateDeliveryState(APIView):
    def post(self, request):
        post_id = request.data.get('post_id')
        delivery_state = request.data.get('delivery_state')
        print(post_id,delivery_state)

        try:
            # Get the React instance with the specified post_id
            react_instance = React.objects.get(product_id=post_id)

            # Update the delivery_state
            react_instance.delivery_state = delivery_state
            react_instance.save()

            # Serialize the updated instance
            serializer = ReactSerializer(react_instance)

            return Response(serializer.data)
        except React.DoesNotExist:
            # If the React instance with the specified post_id does not exist
            print("Error")

class ReactView_GetDeliveryState(APIView):
    def post(self, request):
        # Get the product_id from the request
        product_id = request.data.get('post_id')
        print(product_id)

        try:
            # Get the React instance with the specified product_id
            react_instance = React.objects.get(product_id=product_id)

            # Get the delivery_state
            delivery_state = react_instance.delivery_state

            return Response({'delivery_state': delivery_state})
        except React.DoesNotExist:
            # If the React instance with the specified product_id does not exist
            return Response({'error': 'Product does not exist'}, status=status.HTTP_404_NOT_FOUND)