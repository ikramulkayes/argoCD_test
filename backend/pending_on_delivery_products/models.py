from django.db import models

# Create your models here.
class React(models.Model):
    post_id = models.IntegerField(max_length=100)
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    businessman_userid = models.CharField(max_length=255, blank=True, null=True)
    farmer_userid = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, default='some_default_value')
    class Meta:
        db_table = 'pending_on_delivery_products' 