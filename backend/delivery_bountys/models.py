from django.db import models

class React(models.Model):
    pending_payment_id = models.AutoField(primary_key=True)
    userid = models.CharField(max_length=255)
    transaction_id = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    product_id = models.IntegerField()
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    class Meta:
        db_table = 'delivery_bounties' 
