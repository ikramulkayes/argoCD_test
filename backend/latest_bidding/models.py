from django.db import models

# Create your models here.
class React(models.Model):
    post_id = models.IntegerField(max_length=100)
    max_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    current_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    last_bidder = models.CharField(max_length=255, blank=True, null=True)
    bidding_ended = models.BooleanField(default=False)
    class Meta:
        db_table = 'latest_bidding' 