from django.shortcuts import render
from rest_framework.views import APIView
from .models import AuctionsInventory
from .serializers import AuctionsInventorySerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

class ReactView_Register_Incoming_Auction_Prodcuts(APIView):
    def get(self, request):
        data = AuctionsInventory.objects.all()
        serializer = AuctionsInventorySerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AuctionsInventorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CheckPostsExistenceView_Incoming_Auction_List(APIView):
    def post(self, request):
        post_id = request.data.get('post_id')

        # Check if users with the given post_id exist
        users = AuctionsInventory.objects.filter(post_id=post_id)

        if users.exists():
            # At least one user with the given post_id exists
            react_instance = users.first()  # Take the first user's data
            temp = react_instance.description.split("\r\n")
            print(temp)
            myDesc = []
            for elm in temp:
                a,b = elm.split(":")
                a = a.strip()
                b = b.strip()
                myDesc.append({a:b})
            
            response_data = {
                "post_id": post_id,
                "exists": True,
                "user_data": {
                    "post_id": react_instance.post_id,
                    "name": react_instance.name,
                    "amount": react_instance.amount,
                    "price": react_instance.price,
                    "bidding_placed": react_instance.total_bidding_placed,
                    "start_time": react_instance.start_time,
                    "end_time": react_instance.end_time,
                    "current_time": react_instance.current_time,
                    "posted_by": react_instance.posted_by,
                    "description": myDesc,
                    
                }
            }
        else:
            response_data = {"post_id": post_id, "exists": False, "user_data": {}}

        return Response(response_data)



class ReactView_DeleteMember_Incoming_Auction_list(APIView):
    def post(self, request):
        post_id = request.data.get('post_id')
        print(post_id)

        try:
            member = AuctionsInventory.objects.get(post_id=post_id)
            member.delete()
            return Response({'success': True})
        except AuctionsInventory.DoesNotExist:
            return Response({'success': False, 'error': 'Member does not exist'})

class ReactView_Edit_Incoming_Auction_list_current_price(APIView):
    def post(self, request):

            post_id = request.data.get('post_id', '')
            react_instance = get_object_or_404(AuctionsInventory, post_id=post_id)
            
            # Update the object with new data

            react_instance.price = request.data.get('price', react_instance.price)
            react_instance.total_bidding_placed = request.data.get('total_bidding_placed', react_instance.total_bidding_placed)

            # Save the changes
            react_instance.save()

            return Response(status=status.HTTP_201_CREATED)