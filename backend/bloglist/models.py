from django.db import models

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    userid = models.CharField(max_length=30)
    comment_content = models.TextField()
    post_id = models.IntegerField()
    # Add other fields for comments if needed

    class Meta:
        db_table = 'bloglist_comments'  # Replace 'custom_comment_table' with your preferred table name

class React(models.Model):
    post_id = models.AutoField(primary_key=True)
    userid = models.CharField(max_length=30)
    user_type = models.CharField(max_length=20)
    post_title = models.CharField(max_length=255)
    post_content = models.TextField()
    post_uploaded = models.DateTimeField(auto_now_add=True)
    post_image = models.TextField(null=True, blank=True)
    comments = models.ManyToManyField(Comment)  # Use ManyToManyField with Comment model

    class Meta:
        db_table = 'blog_list'  # Replace 'custom_react_table' with your preferred table name
