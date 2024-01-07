from django.db import models

# Create your models here.
class React(models.Model):
    rid = models.AutoField(primary_key=True)
    userid = models.CharField(max_length=30)
    businessman_userid = models.CharField(max_length=30)
    review_content = models.CharField(max_length=250)
    star = models.PositiveIntegerField(default=0)
    product_id = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'farmer_review' 
        

