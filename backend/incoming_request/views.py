from django.shortcuts import render
from rest_framework.views import APIView
from .models import React
from .serializers import ReactSerializer
from rest_framework.response import Response
from rest_framework import status

class ReactView_Register_Incoming_Request(APIView):
    def get(self, request):
        data = React.objects.all()
        serializer = ReactSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CheckUserExistenceView_Incoming_request(APIView):
    def post(self, request):
        userid = request.data.get('userid')

        # Check if users with the given userid exist
        users = React.objects.filter(userid=userid)

        if users.exists():
            # At least one user with the given userid exists
            user_data = users.values('userid', 'password', 'email', 'address', 'nid', 'user_type')
            response_data = {
                "userid": userid,
                "exists": True,
                "user_data": user_data[0],  # Take the first user's data
            }
            print(user_data[0]['userid'])
        else:
            response_data = {"userid": userid, "exists": False, "user_data": {}}

        return Response(response_data)

class ReactView_DeleteMember_Incoming_request(APIView):
    def post(self, request):
        member_id = request.data.get('memberId')
        print(member_id)

        try:
            member = React.objects.get(userid=member_id)
            member.delete()
            return Response({'success': True})
        except React.DoesNotExist:
            return Response({'success': False, 'error': 'Member does not exist'})