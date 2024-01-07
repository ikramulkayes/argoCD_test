# authentication/serializers.py
from rest_framework import serializers
from .models import *

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['comment_id','userid', 'comment_content']

class ReactSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = React
        fields = ['post_id', 'userid', 'user_type', 'post_title', 'post_content', 'post_uploaded', 'post_image', 'comments']
