from django.shortcuts import render
from rest_framework.views import APIView
from .models import React,Comment
from .serializers import ReactSerializer,CommentSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

class ReactView_Register_BlogList(APIView):
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

class CheckUserExistenceView_BlogList(APIView):
    def post(self, request):
        post_id = request.data.get('post_id')

        # Check if users with the given post_id exist
        users = React.objects.filter(post_id=post_id)

        if users.exists():
            # At least one user with the given post_id exists
            react_instance = users.first()  # Take the first user's data
            serializer = CommentSerializer(react_instance.comments.all(), many=True)
            
            response_data = {
                "post_id": post_id,
                "exists": True,
                "user_data": {
                    "post_id": react_instance.post_id,
                    "userid": react_instance.userid,
                    "user_type": react_instance.user_type,
                    "post_title": react_instance.post_title,
                    "post_content": react_instance.post_content,
                    "post_uploaded": react_instance.post_uploaded,
                    "post_image": react_instance.post_image,
                    "comments": serializer.data,
                }
            }
        else:
            response_data = {"post_id": post_id, "exists": False, "user_data": {}}

        return Response(response_data)

class ReactView_DeleteMember_BlogList(APIView):
    def post(self, request):
        member_id = request.data.get('post_id')
        print(member_id)

        try:
            member = React.objects.get(post_id=member_id)
            print(member)
            member.delete()
            return Response({'success': True})
        except React.DoesNotExist:
            return Response({'success': False, 'error': 'Post does not exist'})
        



from django.db.models import Q



class Search_In_BlogList(APIView):
    def post(self, request):
        search_word = request.data.get('search_word', '')
        
        # Check if users with the given search_word in post_content exist
        matched_posts_content = React.objects.filter(post_content__icontains=search_word)
        matched_posts_title = React.objects.filter(post_title__icontains=search_word)

        matched_posts_data = []
        
        if matched_posts_content.exists() or matched_posts_title.exists():
            # Posts with the specified word in either post_content or post_title exist
            for post in matched_posts_content:
                serializer = CommentSerializer(post.comments.all(), many=True)
                post_data = {
                    "post_id": post.post_id,
                    "userid": post.userid,
                    "user_type": post.user_type,
                    "post_title": post.post_title,
                    "post_content": post.post_content,
                    "post_uploaded": post.post_uploaded,
                    "post_image": post.post_image,
                    "comments": serializer.data,
                }
                matched_posts_data.append(post_data)

            for post in matched_posts_title:
                # Check if the post is not already included in the result
                if post not in matched_posts_content:
                    serializer = CommentSerializer(post.comments.all(), many=True)
                    post_data = {
                        "post_id": post.post_id,
                        "userid": post.userid,
                        "user_type": post.user_type,
                        "post_title": post.post_title,
                        "post_content": post.post_content,
                        "post_uploaded": post.post_uploaded,
                        "post_image": post.post_image,
                        "comments": serializer.data,
                    }
                    matched_posts_data.append(post_data)

        else:
            response_data = {False}
            return Response(response_data)

        response_data =  matched_posts_data
        return Response(response_data)










class ReactView_Register_BlogList_Comments(APIView):
    def get(self, request):
        data = Comment.objects.all()
        serializer = CommentSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReactView_AddComment(APIView):
    def post(self, request):
        # Extract the post_id from the request data
        post_id = request.data.get('post_id')

        # Check if the post_id is present in the request data
        if post_id is None:
            return Response({"error": "post_id is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Retrieve the React instance based on the post_id
        react_instance = get_object_or_404(React, post_id=post_id)

        # Create a Comment instance using the CommentSerializer
        serializer = CommentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(post_id=post_id)  # Save the post_id along with other data
            # Add the comment to the React instance
            react_instance.comments.add(serializer.instance)
            # Save the React instance
            react_instance.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReactView_DeleteComment(APIView):
    def post(self, request):
        # Get the comment instance
        comment_id = request.data.get('comment_id')
        comment_instance = get_object_or_404(Comment, comment_id=comment_id)

        # Remove the comment from associated posts


        # Delete the comment
        comment_instance.delete()

        return Response({"success": True})
    


class ReactView_DeleteAllComment(APIView):
    def post(self, request):
        # Get the post ID for which you want to delete all comments
        post_id = request.data.get('post_id')

        # Get all comments associated with the post
        comments_to_delete = Comment.objects.filter(post_id=post_id)

        # Delete all comments
        comments_to_delete.delete()

        return Response({"success": True})


class ReactView_Blog_Edit(APIView):
    def post(self, request):
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid():
            post_id = request.data.get('post_id', '')
            react_instance = get_object_or_404(React, post_id=post_id)

            # Update the object with new data
            react_instance.userid = request.data.get('userid', react_instance.userid)
            react_instance.user_type = request.data.get('user_type', react_instance.user_type)
            react_instance.post_title = request.data.get('post_title', react_instance.post_title)
            react_instance.post_content = request.data.get('post_content', react_instance.post_content)
            # You may need to handle the datetime format based on your requirements
            react_instance.post_uploaded = request.data.get('post_uploaded', react_instance.post_uploaded)
            react_instance.post_image = request.data.get('post_image', react_instance.post_image)

            # Save the changes
            react_instance.save()

            # Update comments using the ManyToManyField
            comment_ids = request.data.get('comments', [])
            react_instance.comments.set(comment_ids)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)