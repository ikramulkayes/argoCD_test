from django.db import models



class AuctionsInventory(models.Model):
    post_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    #rating = models.DecimalField(max_digits=3, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total_bidding_placed = models.PositiveIntegerField(default=0)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField()
    current_time = models.DateTimeField(auto_now_add=True)
    #place_bid_button = models.BooleanField(default=True)
    posted_by = models.CharField(max_length=255, default='')
    description = models.TextField(max_length=555)

    class Meta:
        db_table = 'farmer_auction_posts_inventory_list'
