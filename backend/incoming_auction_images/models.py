from django.db import models



class React(models.Model):
    post_id = models.IntegerField()
    image = models.ImageField(upload_to='incoming_auction_images/')
    class Meta:
        db_table = 'incoming_auction_images'