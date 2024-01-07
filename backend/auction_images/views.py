from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from . serializers import *
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.http import HttpResponse

class GetImageView_Auction(APIView):
    def post(self, request):
        post_id = request.data.get('post_id')
        # Get the YourModelName instance based on the post_id
        your_model_instance = get_object_or_404(React, post_id=post_id)

        # Check if the instance has an image
        if your_model_instance.image:
            # Assuming 'images' is your media directory
            image_path = your_model_instance.image.path
            with open(image_path, 'rb') as image_file:
                # Return the image as Response
                return HttpResponse(image_file.read(), content_type='image/jpeg')
        else:
            # Return a default image or a message if there's no image
            return Response('No Image Found')


class YourModelNameView_Auction(APIView):
    def get(self, request):
        # Retrieve all entries from the model and serialize them
        entries = React.objects.all()
        serializer = ReactSerializer(entries, many=True)
        return Response(serializer.data)

    def post(self, request):
        post_id = request.data.get('post_id')
        image = request.data.get('image')

        # Check if the post_id is provided
        if not post_id:
            return Response({"error": "post_id is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Create a dictionary with post_id and image
        data = {"post_id": post_id, "image": image}

        # Serialize the data
        serializer = ReactSerializer(data=data)

        if serializer.is_valid():
            # Save the data to the database
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)