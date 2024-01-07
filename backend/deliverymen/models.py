from django.db import models

# Create your models here.
class React(models.Model):
    userid = models.CharField(max_length=30)
    password = models.CharField(max_length=200)
    email  = models.EmailField(max_length=200)
    address = models.CharField(max_length=200)
    nid = models.IntegerField(max_length=10)
    user_type = models.CharField(max_length=20)
    class Meta:
        db_table = 'deliverymen_credentials' 

